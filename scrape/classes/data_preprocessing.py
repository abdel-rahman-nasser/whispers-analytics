from pickle import TRUE
import pandas as pd
import numpy as np
import arabicstopwords.arabicstopwords as stp
import re


class Arabic_Preprocessing:

    def cleaning_arabic_content(self, text):
        if text is None:
            text = ""
            return text
        search = ["أ", "إ", "آ", "ة", "_", "-", "/", ".", "،", " و ", " يا ", '"', "ـ", "'", "ى",
                  "\\", '\n', '\t', '&quot;', '?', '؟', '!']
        replace = ["ا", "ا", "ا", "ه", " ", " ", "", "", "", " و", " يا",
                   "", "", "", "ي", "", ' ', ' ', ' ', ' ? ', ' ؟ ', ' ! ']
        # remove tashkeel
        tashkeel = re.compile(
            r'[\u0617-\u0618-\u0619-\u061A\u064B-\u0652-\u064C-\u064D-\u064E-\u064F-\u0650-\u0651-\u0652-\u0653-\u0654-\u0655]')
        text = re.sub(tashkeel, "", text)

        longation = re.compile(r'(.)\1+')
        subst = r"\1\1"

        text = re.sub(longation, subst, text)

        text = re.sub(r"[^\w\s]", '', text)

        # remove english words
        text = re.sub(r"[a-zA-Z]", '', text)

        # remove spaces
        text = re.sub(r"\d+", ' ', text)
        text = re.sub(r"\n+", ' ', text)
        text = re.sub(r"\t+", ' ', text)
        text = re.sub(r"\r+", ' ', text)
        text = re.sub(r"\s+", ' ', text)

        # remove repetetions
        text = text.replace('وو', 'و')
        text = text.replace('يي', 'ي')
        text = text.replace('اا', 'ا')

        for i in range(0, len(search)):
            text = text.replace(search[i], replace[i])

        text = text.strip()

        return text


class Data_preprocessing:
    # Function use for dealing with missing data
    def handle_missing_data(self, df, column, fill_with):
        df[column] = df[column].replace(np.nan, fill_with)

    # Function used to remove and clean tweets from special chracters
    def clean_tweets_content(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)", " ", tweet).split())

    # Function for detecting the language and clean contents
    def detect_clean_content(self, content, lang):
        if lang == "en":
            res = self.clean_tweets_content(content)
            return res
        elif lang == "ar":
            pre_arab = Arabic_Preprocessing()
            res = pre_arab.cleaning_arabic_content(content)
            return res

    # This function is used to get the percentage of dataset column

    def get_col_percentage(self, col, df):
        total = df[col].value_counts()
        percentage = round(df[col].value_counts(
            dropna=False, normalize=True)*100, 0)
        # or percentage=round((df[col]/df[col].sum())*100,2)
        res = pd.concat([total, percentage], axis=1,
                        keys=["Total No.", "Percentage"])
        #res['Percentage'] = res['Percentage'].astype(str) + '%'
        return res

    def get_col_percentage_json(col, df):
        # print(col)
        # total = df[col].value_counts()
        percentage = round(df[col].value_counts(
            dropna=False, normalize=True)*100, 1)
        res_as_json = percentage.to_dict()
        return res_as_json

    def word_count(self, w, lang):
        counts = dict()
        if lang.lower() == "en":
            words = w.split()

        else:
            words = w

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        return counts

    def remove_arabic_stopwords(self, words_list):
        # detecting if the word is an arabic stop word or not "remove it if stopword"
        cleaned_words_list = [
            x for x in words_list if not stp.is_stop(u'{}'.format(x))]
        return cleaned_words_list
