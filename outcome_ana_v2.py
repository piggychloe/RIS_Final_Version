"""
Created on 3/17/22

@author: qinyuzhu
"""

import pandas as pd
import numpy as np
import nltk
from csv import reader
from csv import writer
from nltk.corpus import stopwords

df = pd.read_csv("ALL_for_compare.csv")
# ret = []
# for data in df['score']:
#     if data != "":
#         ret.append("NLTK")
#
# df['model'] = ret

ed = []
for date in df['created_at']:
    if "2018-01" in date:
        ed.append("01/2018")
    elif "2018-02" in date:
        ed.append("02/2018")
    elif "2018-03" in date:
        ed.append("03/2018")
    elif "2018-04" in date:
        ed.append("04/2018")
    elif "2018-05" in date:
        ed.append("05/2018")
    elif "2018-06" in date:
        ed.append("06/2018")
    elif "2018-07" in date:
        ed.append("07/2018")
    elif "2018-08" in date:
        ed.append("08/2018")
    elif "2018-09" in date:
        ed.append("09/2018")
    elif "2018-10" in date:
        ed.append("10/2018")
    elif "2018-11" in date:
        ed.append("11/2018")
    elif "2018-12" in date:
        ed.append("12/2018")
    elif "2019-01" in date:
        ed.append("01/2019")
    elif "2019-02" in date:
        ed.append("02/2019")
    elif "2019-03" in date:
        ed.append("03/2019")
    elif "2019-04" in date:
        ed.append("04/2019")
    elif "2019-05" in date:
        ed.append("05/2019")
    elif "2019-06" in date:
        ed.append("06/2019")
    elif "2019-07" in date:
        ed.append("07/2019")
    elif "2019-08" in date:
        ed.append("08/2019")
    elif "2019-09" in date:
        ed.append("09/2019")
    elif "2019-10" in date:
        ed.append("10/2019")
    elif "2019-11" in date:
        ed.append("11/2019")
    elif "2019-12" in date:
        ed.append("12/2019")
df['YM'] = ed

sentiment = []
for senti in df['score']:
    if "POS" in senti:
        sentiment.append(1)
    else:
        sentiment.append(0)
df['nltk_sentiment'] = sentiment

sentiment_two = []
for senti in df['BERTscore']:
    if "POS" in senti:
        sentiment_two.append(1)
    else:
        sentiment_two.append(0)
df['bert_sentiment'] = sentiment_two

df.to_csv('ALL_for_relvscore.csv', index=False)
# print(df)


if __name__ == '__main__':
    pass
