#from camel_tools.sentiment import SentimentAnalyzer
from transformers import AutoTokenizer,AutoModelForSequenceClassification,pipeline
import torch
import numpy as np
import re
import pandas as pd

tokenizer = AutoTokenizer.from_pretrained("CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment")
model =AutoModelForSequenceClassification.from_pretrained("CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment")
#snt = SentimentAnalyzer("CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment")
#sa = pipeline('text-classification', model='CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment')

#Arabic Sentiment Analysis Class
class Arabic_Sentiment:
    
    def arabic_sentiment_analysis(self,content):
        #Using Camel Tools
        #res=snt.predict_sentence(content)
        
        #Using pipeline from transformers
        #res=sa([content])[0]["label"]
        
        labels=["positive","negative","neutral"]
        tokens = tokenizer.encode(content, return_tensors='pt')
        result = model(tokens)
        res=labels[int(torch.argmax(result.logits,dim=-1))]
        return res