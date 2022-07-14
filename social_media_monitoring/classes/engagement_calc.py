
class Engagment_Calc:
    def calculate_engagement_rate(self,no_followers,total_num_posts,total_likes,total_comments):
        
        #Formula to calculate the engagement rate for recent posts
        engagement_rate=(float(total_likes+total_comments)/(no_followers*total_num_posts))*100

        #return a float
        return round(engagement_rate,2)
