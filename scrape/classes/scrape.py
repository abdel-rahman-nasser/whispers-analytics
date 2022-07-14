import pandas as pd
import tweepy as tw
from . import credentials
from . import data_preprocessing as d
from . import arabic_sentiment as ar_senti
import twint



#Scraping Using Twint
class Twint_Tweets_Scraping:
    # Implementation of the constructor
    def __init__(self, key_word="Tesla", lang="en", min_l=0, limit=100):
        self.conf = twint.Config()
        self.s = key_word
        self.lang = lang
        self.min = min_l
        self.lim = limit

    # For Collecting tweets and creating the DataFrame
    def scraping_tweets(self, key=None, lang=None, min_l=None, limit=None):
        if key is None:
            key = self.s

        if lang is None:
            lang = self.lang

        if min_l is None:
            min_l = self.min

        if limit is None:
            limit = self.lim

        self.conf.Limit = limit
        self.conf.Lang = lang
        self.conf.Search = key
        self.conf.Hide_output = True
        self.conf.Min_likes = min_l
        self.conf.Pandas = True
        twint.run.Search(self.conf)
        df = twint.storage.panda.Tweets_df
        return df



#Scraping Using Tweepy
class Twitter_Authentication:
    #Function used to connect with the Twitter API
    def app_authenticate(self):
        auth =tw.OAuthHandler(credentials.API_KEY, credentials.KEY_SECRET)
        auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)
        return auth

class Data_collection:
    def __init__(self,user=None):
        au=Twitter_Authentication()
        self.auth =au.app_authenticate()
        self.api = tw.API(self.auth, wait_on_rate_limit=True)
        self.user=user

    #Function to search for a specific word, query or hashtag in Twitter and get tweets
    def get_tweets(self,word_to_search,tweets_num):
        tweets=tw.Cursor(self.api.search,q=word_to_search,lang="en",result_type="mixed").items(tweets_num)
        collected_tweets=[i for i in tweets]
        return collected_tweets

    #Function to get tweets from specific user
    def get_tweets_from_user(self,tweets_num):
        tweets=tw.Cursor(self.api.user_timeline,screen_name=self.user).items(tweets_num)
        collected_tweets=[i for i in tweets]
        return collected_tweets

    #Function that used in collecting all the collected data into a Pandas DataFrame
    def tweets_to_DataFrame(self,tweets):
        pre=d.Data_preprocessing()
        tweets_data=[{
            "tweet":pre.detect_clean_content(tweet.text,tweet.lang),
            "tweet_len":len(tweet.text),
            "date":tweet.created_at,
            "source":tweet.source,
            "likes":tweet.favorite_count,
            "retweets":tweet.retweet_count,
            "No._followers":tweet.user.followers_count,
            "lang":tweet.lang
        } for tweet in tweets]

        df=pd.DataFrame(tweets_data)
        return df
