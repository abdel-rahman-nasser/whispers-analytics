import twint
import tweepy as tw
import pandas as pd
from scrape.classes.data_preprocessing import Data_preprocessing 
from scrape.classes.scrape import Twitter_Authentication

class Tweets_Scraping_user:
    #Impelementation of the constructor
    def __init__(self,scraper="twint"):
        self.scraper=scraper
        if scraper.lower()=="twint":
            self.conf=twint.Config()
        else:
            au=Twitter_Authentication()
            self.auth =au.app_authenticate()
            self.api = tw.API(self.auth, wait_on_rate_limit=True)
    
    def get_tweets_from_user_tweepy(self,user):
        tweets=tw.Cursor(self.api.user_timeline,screen_name=user).items(50)
        collected_tweets=[i for i in tweets]
        return collected_tweets

    def tweets_to_DataFrame(self,tweets):
        pre=Data_preprocessing()
        tweets_data=[{
            "tweet":pre.clean_tweets_content(tweet.text),
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

    def scrape_user(self,user):
        if self.scraper.lower()=="twint": 
            self.conf.Username =user
            self.conf.Limit=50
            self.conf.Lang = "en"
            self.conf.Hide_output=True
            self.conf.Pandas=True
            twint.run.Search(self.conf)
            df = twint.storage.panda.Tweets_df
            return df
        else:
            tweets=self.get_tweets_from_user_tweepy(user)
            df=self.tweets_to_DataFrame(tweets)
            return df

    def scrape_twt_user_info(self,user):
        
        if self.scraper.lower()=="twint": 
            self.conf.Username = user
            self.conf.Hide_output=True
            self.conf.Store_object = True
            twint.run.Lookup(self.conf)
            u = twint.output.users_list[0]
            df_info=pd.DataFrame({"id":u.id,
                                  "name":u.name,
                                  "bio":u.bio,
                                  "followers_num":u.followers,
                                  "tweets_num":u.tweets,
                                  "likes_num":u.likes},index=[0])
            return df_info
            
        else:
            u=self.api.get_user(screen_name=user)
            df_info=pd.DataFrame({"id":u.id,
                                  "name":u.screen_name,
                                  "bio":u.description,
                                  "followers_num":u.followers_count,
                                  "tweets_num":u.statuses_count,
                                  "likes_num":u.favourites_count},index=[0])
            return df_info
