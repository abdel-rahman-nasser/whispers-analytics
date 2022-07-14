import time as t
from bs4 import *
import re
import pandas as pd
from datetime import datetime

from social_media_monitoring.classes.Driver_Init import Driver_Init
from social_media_monitoring.classes.FI_Data_Handling import FI_Data_Handling


class Face_Scraping:
    def __init__(self, driver="chrome"):
        self.driver = Driver_Init().initialize_driver(driver)

    def get_page_info(self, url=None, name=None):

        if url is None:
            url = "https://www.facebook.com/"+name+"/about/"

        if name is None:
            if url[-1] == "/":
                name = re.findall(r'/[^/]+/([^/]+)/', url)[0]
            else:
                name = re.findall(r'/[^/]+/([^/]+)', url)[0]

            url = "https://www.facebook.com/"+name+"/about/"

        self.driver.get(url)

        if "Page not found" in self.driver.title:
            print("Sorry, This Page is Not Available!!")
            # self.driver.close()

        else:
            page_info = {
                "pg_likes": 0,
                "pg_follows": 0,
                'pg_checked': 0,
                'pg_about': '.'
            }

            try:
                t.sleep(1)
                soup = BeautifulSoup(self.driver.page_source, "html.parser")

                all_info = soup.find_all("div", {
                    "class": "dati1w0a ihqw7lf3 hv4rvrfc discj3wi d2edcug0" +
                    " f9o22wc5 nzypyw8j ad2k81qe tr9rh885 rq0escxv l82x9zwi" +
                    " uo3d90p7 pw54ja7n ue3kfks5 hybvsw6c"
                })

                collected_info = all_info[0].find_all(
                    "div", {"class": "qzhwtbm6 knvmm38d"})
                collected_info = [
                    x.text for x in collected_info if x.text != "About"]
                for q in collected_info:
                    if "like" in q:
                        page_info["pg_likes"] = int(
                            "".join(re.findall(r'\d+', q)))

                    elif "follow" in q:
                        page_info["pg_follows"] = int(
                            "".join(re.findall(r'\d+', q)))

                    elif "checked" in q:
                        page_info["pg_checked"] = int(
                            "".join(re.findall(r'\d+', q)))

                    elif 'About' in q:
                        page_info["pg_about"] = q[5:]

                # self.driver.close()
                return page_info

            except Exception as e:
                print(e)
                # self.driver.close()

    def get_page_posts(self, url=None, name=None):

        if url is None:
            url = "https://www.facebook.com/pg/"+name+"/posts/"

        if name is None:
            if url[-1] == "/":
                name = re.findall(r'/[^/]+/([^/]+)/', url)[0]
            else:
                name = re.findall(r'/[^/]+/([^/]+)', url)[0]

            url = "https://www.facebook.com/pg/"+name+"/posts/"

        self.driver.get(url)

        if "Page not found" in self.driver.title:
            print("Sorry, This Page is Not Available!!")
            # self.driver.close()

        else:
            t.sleep(1)
            comments = []
            reactions = []
            shares = []
            contents = []
            timestamps = []
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            all_posts = soup.find_all("div", {"class": "_427x"})

            for post in all_posts:
                try:
                    comment = post.find("a", {"class": "_3hg- _42ft"})
                    if comment is None:
                        comment = BeautifulSoup("<p>0 Comments</p>", "lxml")
                except Exception:
                    comment = "Not Found"
                    print(comment)

                try:
                    timestamp = post.find(
                        "abbr", {"class": re.compile(r"_5ptz")})
                except Exception:
                    timestamp = "Not Found"
                    print(timestamp)

                try:
                    reaction = {}
                    tot = post.find("span", {"class": "_81hb"})
                    if tot is None:
                        tot = BeautifulSoup("<p>0</p>", "lxml")

                    like = post.find(
                        "a", {"class": "_1n9l", "aria-label": re.compile(r'Like')})
                    if like is None:
                        like = BeautifulSoup(
                            "<a aria-label='0 Like'>0</a>", "html.parser").find('a')

                    love = post.find(
                        "a", {"class": "_1n9l", "aria-label": re.compile(r'Love')})
                    if love is None:
                        love = BeautifulSoup(
                            "<a aria-label='0 Love'>0</a>", "html.parser").find('a')

                    sad = post.find(
                        "a", {"class": "_1n9l", "aria-label": re.compile(r'Sad')})
                    if sad is None:
                        sad = BeautifulSoup(
                            "<a aria-label='0 Sad'>0</a>", "html.parser").find('a')

                    angry = post.find(
                        "a", {"class": "_1n9l", "aria-label": re.compile(r'Angry')})
                    if angry is None:
                        angry = BeautifulSoup(
                            "<a aria-label='0 Angry'>0</a>", "html.parser").find('a')

                    haha = post.find(
                        "a", {"class": "_1n9l", "aria-label": re.compile(r'Haha')})
                    if haha is None:
                        haha = BeautifulSoup(
                            "<a aria-label='0 Haha'>0</a>", "html.parser").find('a')

                    fi_h = FI_Data_Handling()
                    reaction["tot"] = fi_h.str_num_conv(tot.text)
                    reaction["like"] = fi_h.str_num_conv(
                        like["aria-label"].split()[0])
                    reaction["love"] = fi_h.str_num_conv(
                        love["aria-label"].split()[0])
                    reaction["sad"] = fi_h.str_num_conv(
                        sad["aria-label"].split()[0])
                    reaction["haha"] = fi_h.str_num_conv(
                        haha["aria-label"].split()[0])
                    reaction["angry"] = fi_h.str_num_conv(
                        angry["aria-label"].split()[0])
                    remaining_reacts = fi_h.str_num_conv(tot.text)-(fi_h.str_num_conv(like["aria-label"].split()[0]) +
                                                                    fi_h.str_num_conv(love["aria-label"].split()[0]) +
                                                                    fi_h.str_num_conv(sad["aria-label"].split()[0]) +
                                                                    fi_h.str_num_conv(angry["aria-label"].split()[0]) +
                                                                    fi_h.str_num_conv(
                        haha["aria-label"].split()[0])
                    )

                    reaction["r_reacts"] = abs(remaining_reacts)

                except Exception as e:
                    print(e)

                try:
                    share = post.find("span", {"class": "_355t _4vn2"})
                    if share is None:
                        share = BeautifulSoup("<p>0 Shares</p>", "lxml")
                except Exception:
                    share = "Not Found"
                    print(share)

                try:
                    content = post.find(
                        "div", {"class": "_5pbx userContent _3576"})
                    if content is None:
                        content = post.find("div", {"class": "_5_jv _58jw"})
                        if content is None:
                            content = BeautifulSoup(
                                "<p>No Content</p>", "lxml")
                except Exception:
                    content = "Not Found"
                    print(content)

                timestamps.append(timestamp["data-utime"])
                contents.append(content.text)
                comments.append(fi_h.str_num_conv(comment.text.split()[0]))
                shares.append(fi_h.str_num_conv(share.text.split()[0]))
                reactions.append(reaction)
            df = pd.DataFrame({
                "timestamp": timestamps,
                "upload_date": [datetime.fromtimestamp(int(x)) for x in timestamps],
                "Content": contents,
                "Num_Comments": comments,
                "Num_Shares": shares,
                "Total_Reacts": [x["tot"] for x in reactions],
                "Likes": [x["like"] for x in reactions],
                "Sad": [x["sad"] for x in reactions],
                "Angry": [x["angry"] for x in reactions],
                "Love": [x["love"] for x in reactions],
                "Haha": [x["haha"] for x in reactions],
                "Remaining_reacts": [x["r_reacts"] for x in reactions],
            })

            df.drop_duplicates(subset="Content", inplace=True, keep="first")

            # self.driver.close()

            return df
