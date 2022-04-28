"""
Created on 3/24/22

@author: qinyuzhu
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# def get_words(path):
#     with open (path, 'r', encoding='utf-8') as f:
#         words = f.readlines()
#         setword = set(m.strip() for m in words)
#         return frozenset(setword)

df = pd.read_csv('ALL_for_valley.csv')

text = df['tweet'].tolist()
cv = CountVectorizer(max_df=0.85)
word_vect = cv.fit_transform(text)
print(word_vect)



if __name__ == '__main__':
    pass
