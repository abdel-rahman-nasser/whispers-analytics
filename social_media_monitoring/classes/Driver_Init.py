from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import *
import requests
import re
import base64
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager


class Driver_Init:
    def initialize_driver(self, driver="chrome"):
        if driver.lower() == "firefox":
            options = FirefoxOptions()
            options.add_argument("--headless")
            options.add_argument('--no-proxy-server')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('log-level=3')
            driver = webdriver.Firefox(options=options)
            return driver

        else:
            print("\nYOU USE CHROME DRIVER!!!!\n")
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-proxy-server')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('log-level=3')
            chrome_options.add_argument('--headless')

            # there is a chromedriver.exe file "already installed"
            # if this driver is not compatible with PC's or lap's chrome version
            # then you can install the appropriate driver from this link
            # https://chromedriver.chromium.org/downloads
            # then include the installed exe file or attach it with the django project
            # or inside this "classes" folder  
            driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
            #driver = webdriver.Chrome(options=chrome_options)
            return driver

    def get_sessionID(self):
        try:
            link = 'https://www.instagram.com/accounts/login/'
            login_url = 'https://www.instagram.com/accounts/login/ajax/'
            pas = base64.b64decode("V2hpc3B5MDAx").decode("utf-8")
            # user = base64.b64decode("V2hpc3BlcnMzMzY2").decode("utf-8")
            # user=base64.b64decode("V2hpc3BlcnMzMzY2").decode("utf-8")
            user = base64.b64decode(
                "V2hpc3BlcnNBbmFseXRpY3NOTFBAZ21haWwuY29t").decode("utf-8")
            time = int(datetime.now().timestamp())

            payload = {
                'username': user,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pas}',
                'queryParams': {},
                'optIntoOneTap': 'false'
            }

            with requests.Session() as s:
                r = s.get(link)
                csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
                r = s.post(login_url, data=payload, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                    "Referer": "https://www.instagram.com/accounts/login/",
                    "x-csrftoken": csrf
                })

            session_id = s.cookies.get_dict()["sessionid"]
            return session_id
        except Exception as e:
            print(e)
            print("Unable to get Session ID!!")
