"""
Created on 3/17/22

@author: qinyuzhu
"""

from nltk.sentiment import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    word = sentiment_dict

    if sentiment_dict['compound'] >= 0.05:
        test =  "POSITIVE"

    elif sentiment_dict['compound'] <= - 0.05:
        test = "NEGATIVE"

    else:
        test = "neu"

    return test

if __name__ == '__main__':
    sentence = "I use AI"
    print(sentiment_scores(sentence))
