"""
Created on 4/5/22

@author: qinyuzhu
"""

import pandas as pd
import numpy as np
import nltk
from csv import reader
from csv import writer

"""
PURPOSE: the following code is used to get all the sentiment for nltk model after sklearn cleaned
FILE: the file will be stored and named as "temp_skl_nltk.csv"
"""
# df = pd.read_csv("ALL_sklearn.csv")
# nsentiment = []
# nmodel = []
#
# int=0
# for int in range(len(df['nltk_sentiment'])):
#     # author.append(df['author'])
#     # create.append(df['created_at'])
#     # YM.append(df['YM'])
#     nsentiment.append(df['nltk_sentiment'][int])
#     nmodel.append('NLTK')
#
# df['model'] = nmodel
# df['sentiment'] = nsentiment
# nframe = df[['author_id', 'created_at', 'text', 'model', 'YM','sentiment']]
# print(nframe)
# nframe.to_csv('temp_skl_nltk.csv', index=False)


"""
PURPOSE: the following code is used to get all the sentiment for nltk model after sklearn cleaned
FILE: the file will be stored and named as "temp_skl_bert.csv"
"""

# df = pd.read_csv("ALL_sklearn.csv")
# bsentiment = []
# bmodel = []
#
# int=0
# for int in range(len(df['bert_sentiment'])):
#     bsentiment.append(df['bert_sentiment'][int])
#     bmodel.append('BERT')
#
# df['model'] = bmodel
# df['sentiment'] = bsentiment
# bframe = df[['author_id', 'created_at', 'text', 'model', 'YM','sentiment']]
# print(bframe)
# bframe.to_csv('temp_skl_bert.csv', index=False)

"""
PURPOSE: the following code is used to combine "temp_skl_nltk.csv" and "temp_skl_bert.csv" after sklearn cleaned
FILE: the file will be stored and named as "temp_skl_combined.csv"
"""
# ndf = pd.read_csv("temp_skl_nltk.csv")
# bdf = pd.read_csv("temp_skl_bert.csv")
# frame = [ndf, bdf]
# result = pd.concat(frame, ignore_index=True)
# print(result)
# result.to_csv('temp_skl_combined.csv', index=False)

"""
PURPOSE: the following code is used to get gov sentiment for nltk model after sklearn cleaned
FILE: the file will be stored and named as "temp_skl_ngov.csv"
"""
# df = pd.read_csv("ALL_sklearn_gov.csv")
# nsentiment = []
# nmodel = []
#
# int=0
# for int in range(len(df['nltk_sentiment'])):
#     # author.append(df['author'])
#     # create.append(df['created_at'])
#     # YM.append(df['YM'])
#     nsentiment.append(df['nltk_sentiment'][int])
#     nmodel.append('NLTK')
#
# df['model'] = nmodel
# df['gov_sentiment'] = nsentiment
# nframe = df[['author_id', 'created_at', 'text', 'model', 'YM','gov_sentiment']]
# print(nframe)
# nframe.to_csv('temp_skl_ngov.csv', index=False)

"""
PURPOSE: the following code is used to get gov sentiment for bert model after sklearn cleaned
FILE: the file will be stored and named as "temp_skl_bgov.csv"
"""
# df = pd.read_csv("ALL_sklearn_gov.csv")
# bsentiment = []
# bmodel = []
#
# int=0
# for int in range(len(df['bert_sentiment'])):
#     bsentiment.append(df['bert_sentiment'][int])
#     bmodel.append('BERT')
#
# df['model'] = bmodel
# df['gov_sentiment'] = bsentiment
# bframe = df[['author_id', 'created_at', 'text', 'model', 'YM','gov_sentiment']]
# print(bframe)
# bframe.to_csv('temp_skl_bgov.csv', index=False)

"""
PURPOSE: the following code is used to combine "temp_skl_ngov.csv" and "temp_skl_bgov.csv" after sklearn cleaned
FILE: the file will be stored and named as "temp_skl_combined_gov.csv"
"""
# ndf = pd.read_csv("temp_skl_ngov.csv")
# bdf = pd.read_csv("temp_skl_bgov.csv")
# frame = [ndf, bdf]
# result = pd.concat(frame, ignore_index=True)
# print(result)
# result.to_csv('temp_skl_combined_gov.csv', index=False)

"""
PURPOSE: the following code is used to get company sentiment for nltk model after sklearn cleaned
FILE: the file will be stored and named as "temp_skl_ncomp.csv"
"""
# df = pd.read_csv("ALL_sklearn_comp.csv")
# nsentiment = []
# nmodel = []
#
# int=0
# for int in range(len(df['nltk_sentiment'])):
#     nsentiment.append(df['nltk_sentiment'][int])
#     nmodel.append('NLTK')
#
# df['model'] = nmodel
# df['comp_sentiment'] = nsentiment
# nframe = df[['author_id', 'created_at', 'text', 'model', 'YM','comp_sentiment']]
# print(nframe)
# nframe.to_csv('temp_skl_ncomp.csv', index=False)

"""
PURPOSE: the following code is used to get company sentiment for bert model after sklearn cleaned
FILE: the file will be stored and named as "temp_skl_bcomp.csv"
"""
# df = pd.read_csv("ALL_sklearn_comp.csv")
# bsentiment = []
# bmodel = []
#
# int=0
# for int in range(len(df['bert_sentiment'])):
#     bsentiment.append(df['bert_sentiment'][int])
#     bmodel.append('BERT')
#
# df['model'] = bmodel
# df['comp_sentiment'] = bsentiment
# bframe = df[['author_id', 'created_at', 'text', 'model', 'YM','comp_sentiment']]
# print(bframe)
# bframe.to_csv('temp_skl_bcomp.csv', index=False)

"""
PURPOSE: the following code is used to combine "temp_skl_ncomp.csv" and "temp_skl_bcomp.csv" after sklearn cleaned
FILE: the file will be stored and named as "temp_skl_combined_comp.csv"
"""
# ndf = pd.read_csv("temp_skl_ncomp.csv")
# bdf = pd.read_csv("temp_skl_bcomp.csv")
# frame = [ndf, bdf]
# result = pd.concat(frame, ignore_index=True)
# print(result)
# result.to_csv('temp_skl_combined_comp.csv', index=False)

if __name__ == '__main__':
    pass
