from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login as lgn, logout
from django.shortcuts import redirect, render
import pandas as pd
from scrape.classes.scrape import Twint_Tweets_Scraping as twi
from scrape.classes.sentiment_analysis import Sentiment_Analysis as senti
from scrape.classes.arabic_sentiment import Arabic_Sentiment as arab_senti
from scrape.classes.data_preprocessing import Data_preprocessing as d_pre
from scrape.models import Query_Data
from gensim.parsing.preprocessing import remove_stopwords
import random


class Scraping_Operations:
    def sections(request):
        if request.user.is_authenticated and request.method == "GET":
            return render(request, 'home/sections.html')
        else:
            return redirect("welcome")

    def home(request):
        if request.user.is_authenticated:
            return render(request, 'home/home.html')
        else:
            return redirect("welcome")

    def results(request):
        if request.user.is_authenticated:
            if request.method == "GET":
                return render(request, 'home/results.html')

        else:
            return redirect("welcome")

    def home_data(request):
        query = request.GET.get("q") or 'Tesla'
        limit = request.GET.get("limit") or 100
        lang = request.GET.get("lang") or 'en'
        analysis_type = request.GET.get("analysis") or 'textblob'

        if str(query) == "":
            return JsonResponse({"hello": "world"})
        elif str(query) != "":
            if str(lang).lower()=="en":
                t = twi(min_l=30)
            else:
                t=twi()
            df = t.scraping_tweets(
                key=str(query),
                limit=int(
                    limit
                ),
                lang=str(lang).lower()
            )
            df.drop(
                columns=[
                    "id",
                    "place",
                    "Unnamed: 0",
                    "urls",
                    "photos",
                    "video",
                    "thumbnail",
                    "quote_url",
                    "conversation_id",
                    "created_at",
                    "geo",
                    "source",
                    "user_rt_id",
                    "user_rt",
                    "retweet_id",
                    "reply_to",
                    "retweet_date",
                    "translate",
                    "trans_src",
                    "trans_dest",
                    "near"
                ],
                axis=1,
                inplace=True,
                errors='ignore'
            )

            d = d_pre()
            df.tweet = df.tweet.apply(
                lambda x: d.detect_clean_content(x, str(lang).lower())
            )
            print(df.tweet)

            # combine all tweets texts in single string
            tweets_texts = ''
            tweets_texts_cleaned_from_stopwords = ''

            for i in df.tweet:
                if i != None:
                    tweets_texts += i + ' '

            if str(lang).lower() == "en":
                # remove stop words "english"
                tweets_texts_cleaned_from_stopwords = remove_stopwords(
                    tweets_texts
                )

            elif str(lang).lower() == "ar":
                # remove stop words "arabic"

                # collecting each word in each row "in 'df.tweet' column"
                tweets_list = []
                for i in df.tweet:
                    for j in i.split():
                        tweets_list.append(j)
                # print(tweets_list)
                tweets_texts_cleaned_from_stopwords = d.remove_arabic_stopwords(
                    tweets_list
                )

            counts = d.word_count(
                tweets_texts_cleaned_from_stopwords, str(lang).lower()
            )
            counts_sorted = sorted(
                counts.items(),
                key=lambda x: x[1],
                reverse=True
            )
            # get first 10 words
            top_100_words = counts_sorted[:100]

            # print(counts_sorted)

            # print(df.head())
            # senti = Sentiment_Analysis("TextBlob")
            # df["sentiment_res"] = df.tweet.apply(
            #     lambda x: senti.sentiment_analysis_method(x)
            # )

            # dates range of all tweets
            oldest_date = df['date'].min()
            newest_date = df['date'].max()

            stats = {
                'oldest_tweet_date': oldest_date,
                'newest_tweet_date': newest_date,
                'numbers_of_languages': len(df['language'].unique()),
                'number_of_tweets': len(df),
                'number_of_likes': int(df['nlikes'].sum()),
                'number_of_retweets': int(df['nretweets'].sum()),
                'number_of_replies': int(df['nreplies'].sum()),
            }

            if str(lang).lower() == "en":
                analysis = senti(analysis_type)
                df[analysis_type+"_res"] = df.tweet.apply(
                    lambda x: analysis.sentiment_analysis_method(x))
                # print(df[a+"_res"].head())
                # df_as_json = df.to_dict(orient='records')
                scales = {
                    'textblob': {
                        -2: "Very Bad",
                        -1: "Bad",
                        0: "Neutral",
                        1: "Good",
                        2: "Very Good"
                    },
                    'bert': {
                        1: "Very Bad",
                        2: "Bad",
                        3: "Neutral",
                        4: "Good",
                        5: "Very Good"
                    }
                }

                df["labeled_"+analysis_type] = df[analysis_type + "_res"].map(
                    lambda x: scales[analysis_type].get(x)
                )

                def get_tweet_sample(type):
                    if not df[df["labeled_"+analysis_type] == type].empty:
                        return df[df["labeled_"+analysis_type] == type].sample().to_json(orient='records')
                    return None

                return JsonResponse({
                    'analysis_type': analysis_type,
                    'analysis_data': d_pre.get_col_percentage_json("labeled_"+analysis_type, df),
                    'counts_sorted': top_100_words,
                    'random_good_sample': get_tweet_sample("Very Good") or get_tweet_sample("Good"),
                    'random_bad_sample': get_tweet_sample("Very Bad") or get_tweet_sample("Bad"),
                    'stats': stats
                })

            elif str(lang).lower() == "ar":
                analysis = arab_senti()
                df["Arabic_Sentiment"] = df.tweet.apply(
                    analysis.arabic_sentiment_analysis)
                df["Arabic_Sentiment"] = df["Arabic_Sentiment"].map(
                    lambda x: x.capitalize())

                def get_tweet_sample(type):
                    if not df[df["Arabic_Sentiment"] == type].empty:
                        return df[df["Arabic_Sentiment"] == type].sample().to_json(orient='records')
                    return None

                return JsonResponse({
                    'analysis_type': analysis_type,
                    'analysis_data': d_pre.get_col_percentage_json("Arabic_Sentiment", df),
                    'counts_sorted': top_100_words,
                    'random_good_sample': get_tweet_sample("Positive") ,
                    'random_bad_sample': get_tweet_sample("Negative"),
                    'stats': stats
                })

                # UI tweet https://codepen.io/moshfequr9/pen/wXQbPR

        # default return
        return JsonResponse({"hello": "world"})
