from pytrends.request import TrendReq

#Google Trends API
class Trends_Collection:
    
    #Class constructor for creating objectsand calling them
    def __init__(self,keywords=[''],category='0',lang='en-US'):
        self.keys=keywords
        self.cat=category
        self.lang=lang
        self.trends=TrendReq()  
        
    
    #this function is used for Searching for Trends using specific words  
    def trends_scraping(self,time="today 3-m",geo='',kw=None,cat=None):
        
        #Specifying keywords
        k_list=kw
        
        #Specifying category
        ct=cat
        
        #Specifying the time to extract data
        tf=time
        
        #Specifying location
        g=geo

        if kw is None:
            k_list=self.keys
        if cat is None:
            ct=self.cat
            
        #build_payload function for searching by words
        self.trends.build_payload(kw_list=k_list,cat=ct,timeframe=tf,geo=g)
        
        #Interest Over Time DataFrame
        time_df = self.trends.interest_over_time()
        del  time_df["isPartial"]
        
        #Interest by Region DataFrame
        region_df=self.trends.interest_by_region()
        
        #Related queries Dictionary
        related_dic = self.trends.related_queries()
        
        return (time_df,region_df,related_dic)
       
    
    def get_top_trends(self):
        top=self.trends.trending_searches()
        return top