from bs4 import *
from instascrape import Profile
import pandas as pd
from instagramy import InstagramUser
import instaloader
import re
from social_media_monitoring.classes.Driver_Init import Driver_Init


class Insta_Scraping:

    def __init__(self, mode="b"):
        if mode == "a":
            d = Driver_Init()
            d.initialize_driver()
            self.session_id = d.get_sessionID()
        else:
            self.session_id = "empty"

    def get_page_posts_info(self, url):
        try:
            session_id = self.session_id
            profile_page = Profile(url)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
                "cookie": f'sessionid={session_id};'
            }
            profile_page.scrape(headers=headers)
            page_info = pd.DataFrame(profile_page.to_dict(), index=[
                                     x for x in range(1)])
            recent_posts = profile_page.get_recent_posts()
            posts_data = [post.to_dict() for post in recent_posts]
            recent_posts_df = pd.DataFrame(posts_data)

            return page_info, recent_posts_df

        except Exception as e:
            print(e)
            print("Unable To Get Insta Profile Info!!!")

    def insta_2_scraper(self, url):
        try:
            session_id = self.session_id
            user = InstagramUser(url, sessionid=session_id, from_cache=True)
            page_info = {}
            page_info["number_of_followers"] = user.number_of_followers
            page_info["number_of_followings"] = user.number_of_followings
            page_info["number_of_posts"] = user.number_of_posts
            page_info["profile_picture_url"] = user.profile_picture_url
            page_info["is_verified"] = user.is_verified
            page_info["other_info"] = user.other_info
            page_info["username"] = user.username
            page_info["fullname"] = user.fullname
            page_info["is_private"] = user.is_private
            page_info["is_joined_recently"] = user.is_joined_recently
            page_info["biography"] = user.biography
            page_info["website"] = user.website
            page_info_df = pd.DataFrame(page_info, index=[x for x in range(1)])

            likes = []
            comments = []
            upload_date = []
            caption = []
            timestamp = []
            display_url = []
            is_video = []
            short_code = []
            post_url = []
            location = []
            for post in user.posts:
                likes.append(post.likes)
                comments.append(post.comments)
                upload_date.append(post.taken_at_timestamp)
                caption.append(post.caption)
                timestamp.append(post.timestamp)
                display_url.append(post.display_url)
                is_video.append(post.is_video)
                short_code.append(post.shortcode)
                post_url.append(post.post_url)
                location.append(post.location)

            posts_info_df = pd.DataFrame({
                "Likes": likes,
                "Num_Comments": comments,
                "upload_date": upload_date,
                "caption": caption,
                "timestamp": timestamp,
                "display_url": display_url,
                "is_video": is_video,
                "short_code": short_code,
                "post_url": post_url,
                "location": location
            })

            return page_info_df, posts_info_df

        except Exception as e:
            print(e)

    def insta_l_scraper(self, username):
        try:
            bot = instaloader.Instaloader()
            user = instaloader.Profile.from_username(bot.context, username)
            print(user)  # this doesn't print out anything

            posts = user.get_posts()
            page_info = {}
            page_info["number_of_followers"] = user.followers
            page_info["number_of_followings"] = user.followees
            page_info["number_of_posts"] = posts.count
            page_info["profile_picture_url"] = user.profile_pic_url
            page_info["is_verified"] = user.is_verified
            page_info["username"] = user.username
            page_info["fullname"] = user.full_name
            page_info["is_private"] = user.is_private
            page_info["business_category"] = user.business_category_name
            page_info["biography"] = user.biography
            page_info["external_url"] = user.external_url
            page_info_df = pd.DataFrame(page_info, index=[x for x in range(1)])

            likes = []
            comments = []
            upload_date = []
            caption = []
            date_utc = []
            date_local = []
            is_video = []
            short_code = []
            post_url = []
            location = []

            # print(user, posts, page_info)

            for e, post in enumerate(posts):
                if e == 11:
                    break
                else:
                    likes.append(post.likes)
                    comments.append(post.comments)
                    upload_date.append(post.date)
                    caption.append(post.caption)
                    date_utc.append(post.date_utc)
                    date_local.append(post.date_local)
                    is_video.append(post.is_video)
                    short_code.append(post.shortcode)
                    post_url.append(post.url)
                    location.append(post.location)

            posts_info_df = pd.DataFrame({
                "Likes": likes,
                "Num_Comments": comments,
                "upload_date": upload_date,
                "caption": caption,
                "date_utc": date_utc,
                "date_local": date_local,
                "is_video": is_video,
                "short_code": short_code,
                "post_url": post_url,
                "location": location
            })

            return page_info_df, posts_info_df

        except Exception as e:
            print(e)
