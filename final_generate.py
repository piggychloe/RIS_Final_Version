"""
Created on 4/25/22

@author: qinyuzhu
"""
import pandas as pd
import numpy as np
import nltk
from csv import reader
from csv import writer
from nltk.corpus import stopwords
"""
this file is used to generated the final visualization stuff in the paper
"""


"""
funtion 1: get the table with BERT and NLTK sentiment both in it for gov and comp
"""

# ndf = pd.read_csv("temp_skl_ncomp.csv")
# bdf = pd.read_csv("temp_skl_bcomp.csv")
#
# nltksent = []
# nltkmodel = []
#
# i = 0
#
# for i in range(len(ndf['comp_sentiment'])):
#     nltksent.append(ndf['comp_sentiment'][i])
#     nltkmodel.append('NLTK')
#
# bdf['model_addN'] = nltkmodel
# bdf['comp_sentiment_addN'] = nltksent
# bn_frame = bdf[['author_id', 'created_at', 'text', 'model', 'YM','comp_sentiment','model_addN', 'comp_sentiment_addN']]
# print(bn_frame)
# bn_frame.to_csv('temp_skl_addBN_comp.csv', index=False)

"""
funtion 2: get the identity sentiment of BERT and NLTK for both gov and comp
"""

# df = pd.read_csv("temp_skl_addBN_comp.csv")
#
# outcome = []
# modele = []
# tweet = []
# author = []
# ym = []
# i = 0
# for i in range(len(df)):
#     if df['comp_sentiment'][i] == df['comp_sentiment_addN'][i]:
#         outcome.append(df['comp_sentiment'][i])
#         modele.append("SAME")
#         tweet.append(df['text'][i])
#         author.append(df['author_id'][i])
#         ym.append(df['YM'][i])
#
# combin = {'author_id': author ,'text': tweet,'model':modele, 'YM': ym, 'comp_sentiment': outcome}
# outcombin = pd.DataFrame(combin)
# outcombin.to_csv('temp_skl_iden_comp.csv', index=False)
# print(outcombin)


"""
funtion 3: change the model name of NLTK+BERT to ALL upon temp_skl_combined for gov and comp
"""
# df = pd.read_csv("temp_skl_combined_comp.csv")
# outcome = []
# modele = []
# tweet = []
# author = []
# ym = []
#
# i = 0
# for i in range(len(df)):
#     outcome.append(df['comp_sentiment'][i])
#     modele.append("ALL")
#     tweet.append(df['text'][i])
#     author.append(df['author_id'][i])
#     ym.append(df['YM'][i])
#
# combin = {'author_id': author ,'text': tweet,'model':modele, 'YM': ym, 'comp_sentiment': outcome}
# outcombin = pd.DataFrame(combin)
# outcombin.to_csv('temp_skl_ALL_comp.csv', index=False)
# print(outcombin)

"""
function 4: this function is used to combine all above to one table
"""

df1 = pd.read_csv("temp_skl_combined_comp.csv")
df2 = pd.read_csv("temp_skl_iden_comp.csv")
df3 = pd.read_csv("temp_skl_ALL_comp.csv")

frame = [df1,df2,df3]
result = pd.concat(frame, ignore_index=True)
result.to_csv('temp_skl_ALLFOUR_comp.csv', index=False)
print(result)


if __name__ == '__main__':
    pass
