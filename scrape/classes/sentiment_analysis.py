from transformers import  AutoTokenizer, AutoModelForSequenceClassification
from textblob import TextBlob
import torch

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

class Sentiment_Analysis:
    
    def __init__(self,analyze_method):
        self.analyze_method=analyze_method
        
    #Function used for applying sentiment analysis based on the input method "Object"
    def sentiment_analysis_method(self,tweet_content):
        try:
            if self.analyze_method.lower()== "textblob":
                analysis = TextBlob(tweet_content)
                #Very Bad
                if analysis.sentiment.polarity >= -1 and analysis.sentiment.polarity <-.5:
                    return -2
                
                #Bad
                elif analysis.sentiment.polarity >=-.5 and analysis.sentiment.polarity <0:
                    return -1
                
                #Neutral
                elif analysis.sentiment.polarity==0:
                    return 0
                
                #Good
                elif analysis.sentiment.polarity >0 and analysis.sentiment.polarity <=.5:
                    return 1
                
                #Very Good
                elif analysis.sentiment.polarity >.5 and analysis.sentiment.polarity <=1:
                    return 2
                
            elif self.analyze_method.lower() =="bert":
                tokens = tokenizer.encode(tweet_content,
                 return_tensors='pt')
                result = model(tokens)
                return int(torch.argmax(result.logits))+1
            
            else:
                return 7
        
        except Exception:
            print("Error!!!, Check Your Inputs Again, Please")