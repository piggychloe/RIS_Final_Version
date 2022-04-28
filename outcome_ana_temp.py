"""
Created on 3/24/22

@author: qinyuzhu
"""
import pandas as pd
import numpy as np
import nltk
from csv import reader
from csv import writer
from nltk.corpus import stopwords



# df = pd.read_csv(r'ALL_for_relvscore.csv')
#
# nltk_outcome = []
# bert_outcome = []
# tweet = []
# author = []
# i = 0
# for i in range(len(df)):
#     if '06/2019' in df['YM'][i]:
#         nltk_outcome.append(df['nltk_sentiment'][i])
#         bert_outcome.append(df['bert_sentiment'][i])
#         tweet.append(df['text'][i])
#         author.append(df['author_id'][i])
#
# combin = {'author_id': author ,'tweet': tweet, 'nltk_outcome': nltk_outcome, 'bert_outcome':bert_outcome}
# outcombin = pd.DataFrame(combin)
# outcombin.to_csv('ALL_for_valley.csv', index=False)
# print(outcombin)

"""
intro: this function is used to pullout the data in June 2019 which two models agree on
period: June 2019
column: author_id, tweet, nltk_outcome, bert_outcome
name of the csv: valley
alt: can changed to peak which is Oct 2018
"""
# df = pd.read_csv("ALL_for_valley.csv")
#
# nltk_outcome = []
# bert_outcome = []
# tweet = []
# author = []
# i = 0
# for i in range(len(df)):
#     if df['nltk_outcome'][i] == df['bert_outcome'][i]:
#         nltk_outcome.append(df['nltk_outcome'][i])
#         bert_outcome.append(df['bert_outcome'][i])
#         tweet.append(df['tweet'][i])
#         author.append(df['author_id'][i])
#
# combin = {'author_id': author ,'tweet': tweet, 'nltk_outcome': nltk_outcome, 'bert_outcome':bert_outcome}
# outcombin = pd.DataFrame(combin)
# outcombin.to_csv('Identity_for_valley.csv', index=False)
# print(outcombin)


"""
intro: this function used to sort out and store tweet which NLTK and BERT has the same sentiment
period: All months
column: author_id, YM, combine_sentiment, tweet
"""

df = pd.read_csv("ALL_for_relvscore.csv")
comb_outcome = []
tweet = []
author = []
YM = []
nltk_outcome = []
bert_outcome = []
i = 0

for i in range(len(df)):
    if df['nltk_sentiment'][i] == df['bert_sentiment'][i]:
        nltk_outcome.append(df['nltk_sentiment'][i])
        bert_outcome.append(df['bert_sentiment'][i])
        comb_outcome.append(df['nltk_sentiment'][i])
        tweet.append(df['text'][i])
        author.append(df['author_id'][i])
        YM.append(df['YM'][i])

tot = {'author_id': author,'text': tweet, 'sentiment': comb_outcome, 'YM':YM}
outtot = pd.DataFrame(tot)
outtot.to_csv('Identity_for_all.csv', index=False)
print(outtot)


"""
intro: this function is used to combine all the sentiment from the two models
outcome would be: for each line of tweets, there would be two sentiment outcomes
period: all YM
column: author_id, YM, combine_sentiment (join bert and nltk)
"""

# df1 = pd.read_csv("bert_togo.csv")
# df2 = pd.read_csv("nltk_togo.csv")
# author = []
# YM = []
# senti = []
#
# i =0
# for i in range(len(df1)):
#     author.append(df1['author_id'][i])
#     YM.append(df1['YM'][i])
#     senti.append(df1['sentiment'][i])
#
# j = 0
# for j in range(len(df2)):
#     author.append(df2['author_id'][j])
#     YM.append(df2['YM'][j])
#     senti.append(df2['sentiment'][j])
#
# ret = {'author_id': author, 'sentiment': senti, 'YM':YM}
# getret = pd.DataFrame(ret)
# getret.to_csv('ALL_for_average.csv', index=False)
# print(getret)




"""
test place
"""
# elem = 0
# fal = 0
# for elem in range(len(outtot)):
#     if outtot['combine_sentiment'][elem] != outtot['bert'][elem]:
#         fal+=1
    # elif df['combine_sentiment'][elem] != df['bert_sentiment'][elem]:
    #     fal +=1
# print(fal)
# outtot.to_csv('Identity_for_all.csv', index=False)




if __name__ == '__main__':
    pass
