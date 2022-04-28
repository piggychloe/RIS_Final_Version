"""
Created on 4/25/22

@author: qinyuzhu
"""

"""
this file is used to generate the table used for barplot in seaborn
input: temp_skl_combined_comp.csv; in the file, we have sentiment for every both with both NLTK and BERT
output: a two column, three rows table for model (NTLK+BERT, NLTK, BERT) and comp_sentiment (ALL N+B, ALL N, ALL B)
"""

import pandas as pd
import numpy as np
import csv

"""
this function is used to split the NLTK and BERT outcome for further generate
input: temp_skl_combinted_comp.csv
output: temp_bar_BERT.csv AND temp_bar_NLTK.csv
"""
# df = pd.read_csv("temp_skl_combined_comp.csv")
# B_data = df[df["model"].str.contains("NLTK") == False]
# N_data = df[df['model'].str.contains('NLTK') ==True]
# B_data.to_csv('temp_bar_BERT.csv', index=False)
# N_data.to_csv('temp_bar_NLTK.csv',index=False)
# print(B_data)
# print(N_data)

"""
this funtion is used to get the overall sentment outcome of n and b
input: temp_bar_BERT.csv AND temp_bar_NLTK.csv
output: a small table 2x3 with overall sentiment outcome
"""

df = pd.read_csv('temp_bar_BERT.csv')
# print(len(df))
int = 0
for value in df['comp_sentiment']:
    int += value
ret = int / 2401

print(ret)

df2 = pd.read_csv('temp_bar_NLTK.csv')
tnt = 0
for v in df2['comp_sentiment']:
    tnt += v
tet = tnt/2401

print(tet)

df3 = pd.read_csv('temp_skl_combined_comp.csv')
ent = 0
for va in df3['comp_sentiment']:
    ent += va
all = ent/4802

print(all)


with open("temp_generate.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    #df_all = pd.DataFrame([csv_reader], index=None)
    df_all = pd.DataFrame({"ALL" : all, "NLTK": ret, "BERT": tet})
    print(df_all)


# a for loop for extracting all the sentiment from three ways


# get a new table with new col names



if __name__ == '__main__':
    pass
