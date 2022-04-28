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

"""
intro: this function is used to add model name (hue) for all files
model: all, same_sentiment, NLTK, BERT
"""
# df = pd.read_csv("ALL_for_average.csv")
#
# all = []
# for data in df['author_id']:
#     if data != "":
#         all.append("ALL")
# df['model'] = all
# df.to_csv('ALL_for_average_cover.csv', index=False)

# alltwo = []
# df2 = pd.read_csv("Identity_for_all.csv")
#
# for elem in df2['author_id']:
#     if elem != "":
#         alltwo.append("SAMEsentiment")
# df2['model'] = alltwo
# df2.to_csv('Identity_for_all_cover.csv', index=False)

"""
intro: this function is used to concat all four files to the same table
period: all YM
"""
df1 = pd.read_csv("nltk_togo.csv")
df2 = pd.read_csv("bert_togo.csv")
df3 = pd.read_csv("ALL_for_average_cover.csv")
df4 =pd.read_csv("Identity_for_all_cover.csv")
frame = [df1,df2,df3,df4]
result = pd.concat(frame, ignore_index=True)
result.to_csv('ALL_FOUR.csv', index=False)


"""
intro: this function is used to add model name (hue) for all files for gov/comp
"""
df = pd.read_csv("temp_skl_combined_gov.csv")

all = []
for data in df['author_id']:
    if data != "":
        all.append("ALL")
df['model'] = all
df.to_csv('temp_skl_combined_gov_ALL.csv', index=False)

alltwo = []
df2 = pd.read_csv("Identity_for_all.csv")

for elem in df2['author_id']:
    if elem != "":
        alltwo.append("SAMEsentiment")
df2['model'] = alltwo
df2.to_csv('Identity_for_all_cover.csv', index=False)

"""
intro: this function is used to concat all four files to the same table
period: all YM
"""
df1 = pd.read_csv("nltk_togo.csv")
df2 = pd.read_csv("bert_togo.csv")
df3 = pd.read_csv("ALL_for_average_cover.csv")
df4 =pd.read_csv("Identity_for_all_cover.csv")
frame = [df1,df2,df3,df4]
result = pd.concat(frame, ignore_index=True)
result.to_csv('ALL_FOUR.csv', index=False)

if __name__ == '__main__':
    pass
