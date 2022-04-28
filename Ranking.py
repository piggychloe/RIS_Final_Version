"""
Created on 3/24/22

@author: qinyuzhu
"""
# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer

import pandas as pd
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from itertools import permutations
from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

#
# df = pd.read_csv('ALL_for_valley.csv')
# df.columns #id, text, category
#
# texts = np.array(df['tweet']) #text contents in dataframe to array for processing
# vocab_length = len(nltk.word_tokenize(list(itertools.chain.from_iterable(texts))) #concatenate all the texts and tokenize the whole corpus
#
#
# vectorizer = TfidfVectorizer(ngram_range = (1,3), max_features = vocab_length) #make Tfidf Vectorizer
# tfidf_encodings = vectorizer.fit_transform(texts) #encode the text
#
# df['tfidf'] = list(tfidf_encodings.toarray()) #vectorized texts to dense list format for storage in dataframe
#
#
# vectors_for_training = np.array(df['tfidf'].tolist()) #get the vectors back out of the dataframe for use in something else
# X_train, y_train, X_test, y_test = train_test_split(vectors_for_training, df['category'].tolist())
#
#
# nb_classifier = MultinomialNB()
# nb_classifier.fit(X_train, y_train)
# nb_predictions = nb_classifier.predict(df.tfidf.tolist())




df = pd.read_csv('Identity_for_valley.csv')

store = []

for elem in df['tweet']:
    elem = [elem]
    v = TfidfVectorizer()
    x = v.fit_transform(elem)
    store.append(x)

df['tfidf'] = store
print(df)

# def computeTF (worddict, bow):
#     tfdict = {}
#     bowcount = len(bow)
#     for word, count in worddict.items():
#         tfdict[word] = count/float(bowcount)
#     return tfdict


if __name__ == '__main__':
    pass
