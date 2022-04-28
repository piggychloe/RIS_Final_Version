"""
Created on 3/14/22

@author: qinyuzhu
"""

import pandas as pd
import numpy as np
import nltk
from csv import reader
from csv import writer
from nltk.corpus import stopwords
# set(stopwords.words('english'))

"""
with finished BERT model outcome, get the sentiment of BERT by adding one column
after NLTK score and the column is called BERTscore
"""

df1 = pd.read_csv(r'bertout_1801.csv')
df2 = pd.read_csv(r'bertout_1802.csv')
df3 = pd.read_csv(r'bertout_1803.csv')
df4 = pd.read_csv(r'bertout_1804.csv')
df5 = pd.read_csv(r'bertout_1805.csv')
df6 = pd.read_csv(r'bertout_1806.csv')
df7 = pd.read_csv(r'bertout_1807.csv')
df8 = pd.read_csv(r'bertout_1808.csv')
df9 = pd.read_csv(r'bertout_1809.csv')
df10 = pd.read_csv(r'bertout_1810.csv')
df11 = pd.read_csv(r'bertout_1811.csv')
df12 = pd.read_csv(r'bertout_1812.csv')
nxy1 = pd.read_csv(r'bertout_1901.csv')
nxy2 = pd.read_csv(r'bertout_1902.csv')
nxy3 = pd.read_csv(r'bertout_1903.csv')
nxy4 = pd.read_csv(r'bertout_1904.csv')
nxy5 = pd.read_csv(r'bertout_1905.csv')
nxy6 = pd.read_csv(r'bertout_1906.csv')
nxy7 = pd.read_csv(r'bertout_1907.csv')
nxy8 = pd.read_csv(r'bertout_1908.csv')
nxy9 = pd.read_csv(r'bertout_1909.csv')
nxy10 = pd.read_csv(r'bertout_1910.csv')
nxy11 = pd.read_csv(r'bertout_1911.csv')
nxy12 = pd.read_csv(r'bertout_1912.csv')
frame = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,nxy1,nxy2,nxy3,
         nxy4,nxy5,nxy6,nxy7,nxy8,nxy9,nxy10,nxy11,nxy12]
result = pd.concat(frame, ignore_index=True)


ret = []
for data in result['bert']:
    if "POS" in data:
        ret.append("POSITIVE")
    if "NEG" in data:
        ret.append("NEGATIVE")

result['BERTscore'] = ret
# print(result)
# print(result)
# result.to_csv('to_sns.csv',index=False)

# print(result)


nltkforsns = result[['author_id', 'created_at', 'text', 'score','BERTscore']]
nltkforsns.to_csv('ALL_for_compare.csv', index=False)
"""
after added column of BERTscore, collect the general pos/neg data for both
"""
# pos = 0
# neg = 0
# for i in range(len(result)):
#     if result['score'][i] == 'POSITIVE':
#         pos += 1
#     else:
#         neg += 1
# print("pos in NLTK is that")
# print(pos*100/38088)
# print("neg in NLTK is that")
# print(neg*100/38088)


"""
find out the tweets which NLTK and BERT does not line up on sentiment
"""
# want = []
# twee = []
# count = 0
# for i in range(len(result)):
#     if (result['score'][i]) != (result['BERTscore'][i]):
#         want.append(result["bert"][i])
#         twee.append(result["text"][i])




    # elif result['score'][i] == "NEG" and result['BERTscore'][i] == "POS":
    #     want.append(result["bert"][i])
    #     twee.append(result["text"][i])
        # count += 1


# result['BERTscore'] = ret

# combin = {'tweet': twee, 'numBERT': want}
# outcombin = pd.DataFrame(combin)
# print(outcombin)
# print(outcombin)
# print(count)


if __name__ == '__main__':
    pass
