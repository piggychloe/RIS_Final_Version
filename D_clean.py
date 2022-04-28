"""
Created on 3/8/22

@author: qinyuzhu
"""
import pandas as pd
import re
import numpy as np
import csv
"""
convert csv to DataFrame in pandas
"""
df = pd.read_csv("out_1801.csv", header=None)
df.columns = ['author_id', 'created_at', 'id', 'lang', 'text']

"""
remove all the line with language detection is not english
"""
df = df[df.lang == "en"]
# print(df)

"""
remove all the line with contains 'RT @'
"""
df = df[df["text"].str.contains("RT @") == False]
# print(df)

"""
replace link and hashtags with nothing
"""
df['text'] = df["text"].str.replace(r"[#][A-Za-z0-9]+|(\w+:\/\/\S+)|(,+)","", regex=True)
df['text'] = df['text'].str.replace ('  +', '', regex=True)
# print(df)

"""
remove the line with less than 20 characters
"""
# df['text'] = df['text'].str.len()>20

"""
get the total number of lines in the table
"""
# index = df.index
# number_of_rows = len(index)
# print(number_of_rows)

"""store the text section into a seperate file"""
# data = df['text']
# data.to_csv('SAMPLE_1912_updated.csv', index=False)
ret = []
ddff = df[['author_id','created_at', "text"]]
print(ddff)
ddff.to_csv('dwed_1801.csv', index=False)

# np.savetxt("dwdone_1912.txt", ddff, delimiter=" ", newline="\n", fmt="%s")


"""
write the updated csv file into a new csv file
"""
# df.to_csv('SAMPLE_1912_updated.csv', index=False)
# print(df)

"""
check the table lineout of the updated csv file"""

# col_list = ['text']
# data = pd.read_csv(r'smlSAMPLE_1912_updated.csv',usecols=col_list)
# print(data)



# filter = df_allen.drop(df_allen.text.str.contains('RT @'))
# df_noRT = df_allen[df.text != "RT @"]
# dt_noRT = df_allen[df.text]
# df = df[df["text"].str.contains("RT @") == False]
# df['text'] = df['text'].str.replace('(RT @).+', 'YES', regex=True)

# df_allen['text'] = df_allen["text"].str.replace('RT @.+', 'Yes', regex=True)


"""somelines might be useful"""
# stop_word = "RT @"
# text_all = [i for i in data['text']]
# text_remove = [i for i in text_all if stop_word not in i]

"""somelines might be useful"""
# ret_word = []
# ret = []
# for text in text_remove:
#     # upd = re.sub(r"http\S+", "", text)
#     upd = re.sub(r"[#][A-Za-z0-9]+|(\w+:\/\/\S+)|(,+)","",text)
#     uupd = re.sub('  +', '', upd)
#     uupd.strip()


    # upd.strip()
    # upd.replace(" ","")
    # " ".join(upd.split())

"""somelines might be useful"""
#     ret.append(uupd)
#     # print(upd)
# text_long = [i for i in ret if len(i) >= 20]

# int = 0
# text_new = []
# for i in range(len(text_long)):
#     if text_long[i] in " ":
#         int +=1
#         if len(text_long[i]) != int:
#             text_new.append(text_long[i])
#             print(text_new)
if __name__ == '__main__':
    pass
