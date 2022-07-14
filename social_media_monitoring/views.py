import json
from django.http import JsonResponse
import pandas as pd
from django.shortcuts import render

from social_media_monitoring.classes.Face_Scraping import Face_Scraping
from social_media_monitoring.classes.Insta_Scraping import Insta_Scraping
from social_media_monitoring.classes.engagement_calc import Engagment_Calc
from social_media_monitoring.classes.Twitter_User_Scraping import Tweets_Scraping_user
from social_media_monitoring.models import social_Data
# Create your views here.
import re
from django.forms.models import model_to_dict

url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    # domain...
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE
)


def social_media_monitoring_index(request):

    # fi = Face_Scraping()
    # df = fi.get_page_posts(url="https://www.facebook.com/google")
    # fi = Face_Scraping()
    # df1 = fi.get_page_info(url="https://www.facebook.com/google")
    # ins = Insta_Scraping()
    # cur_info, cur_posts = ins.insta_2_scraper("google")

    # print(df.head())
    # print(pd.DataFrame(df1, index=[x for x in range(1)]))
    # print(cur_info)
    # print(cur_posts)
    # print(social_Data.objects.filter(s_user=request.user.username).get().twitter)
    return render(request, 'social_media_monitoring/index.html')


def social_media_monitoring_user_details(request):
    user = social_Data.objects.filter(
        s_user=request.user.username,
    ).get()

    return JsonResponse(model_to_dict(user))


def social_media_monitoring_facebook_data(request):
    # Dont forget to switch to chrome
    # if chrome takes a lot of time in scraping process, try to use firefox driver
    #"firefox needs to be installed in this case"
    # (this task should not take more than 10-25 seconds)
    fi = Face_Scraping(driver="chrome")
    #fi = Face_Scraping(driver="firefox")
    fc_url = social_Data.objects.filter(
        s_user=request.user.username).get().face_url
    facebook_page_posts = fi.get_page_posts(url=fc_url)
    facebook_page_info = fi.get_page_info(url=fc_url)

    # fi.driver.close()
    # print(facebook_page_posts)
    data = {
        'facebook_page_info': facebook_page_info,
        'facebook_page_posts': facebook_page_posts.to_json(
            orient='records'
        ),
    }

    return JsonResponse(data)


def social_media_monitoring_instagram_data(request):
    ins = Insta_Scraping()
    insta_url = social_Data.objects.filter(
        s_user=request.user.username
    ).get().insta

    # extract username from url
    username = ''
    if re.match(url_regex, insta_url) is not None:
        username = insta_url.split("/")[-1]

    if not username:
        print("Invalid URL")
        return JsonResponse({})

    res = ins.insta_l_scraper(username)

    if res is not None:
        cur_info, cur_posts = res
        # calculate Engagement Rate Function
        eng = Engagment_Calc()
        print("hhh: ", len(cur_posts["Likes"]))
        engagement_rate = eng.calculate_engagement_rate(
            no_followers=int(cur_info["number_of_followers"]),
            total_num_posts=len(cur_posts["Likes"]),
            total_likes=sum(cur_posts["Likes"]),
            total_comments=sum(cur_posts["Num_Comments"])
        )

        data = {
            'instagram_page_info': cur_info.to_json(orient='records'),
            'instagram_page_posts': cur_posts.to_json(
                orient='records',
            ),
            'engagement_rate': engagement_rate
        }

        return JsonResponse(data)
    else:
        return JsonResponse({})


def social_media_monitoring_twitter_data(request):
    tw = Tweets_Scraping_user()
    twt_url = social_Data.objects.filter(
        s_user=request.user.username
    ).get().twitter

    # extract username from url
    username = ''
    if re.match(url_regex, twt_url) is not None:
        username = twt_url.split("/")[-1]

    if not username:
        print("Invalid URL")
        return JsonResponse({})

    twt_df = tw.scrape_user(username)
    twt_info = tw.scrape_twt_user_info(username)
    # print(twt_info)
    data = {
        'twitter_user_info': twt_info.to_json(orient='records'),
        'twitter_user_data': twt_df.to_json(orient='records'),
    }

    return JsonResponse(data)
