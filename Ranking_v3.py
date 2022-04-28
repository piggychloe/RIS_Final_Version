"""
Created on 3/31/22

@author: qinyuzhu
"""
import numpy as np
import pandas as pd
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import pairwise_kernels

"""
this function is used to test metrics and kernel in sklearn
"""
# X = np.array([[2, 3], [3, 5], [5, 8]])
# Y = np.array([[1, 0], [2, 1]])
# Z = "city"
# pairwise_distances(X, Y, metric='manhattan')
# array([[ 4.,  2.],
#        [ 7.,  5.],
#        [12., 10.]])
# pairwise_distances(X, metric='manhattan')
# array([[0., 3., 8.],
#        [3., 0., 5.],
#        [8., 5., 0.]])
# pairwise_kernels(X, Y, metric='linear')
# array([[ 2.,  7.],
#        [ 3., 11.],
#        [ 5., 18.]])

"""
this function is used to get the content- feature_extraction.text
model: TfidfVectorizer
input: raw content in the table
output: tuple - The lower and upper boundary of the range of n-values for different n-grams to be extracted
"""
# from sklearn.feature_extraction.text import TfidfVectorizer
# a = "Digital IDs Are More Dangerous Than You Think"
# fakew = 'facial recognition facial-recognition faceID ID digit digital digits artificial intelligence AI ML machine learning biometrics security ban bigdata data security privacy personal information private FTC technology tech surveillance camera police computer regulation government legal legislation illegal policy public safetly detection bias gender racial racism racist moral law enforcement protection protect systemicracism access control finger bio biological'
# corpus = [a,fakew]
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(corpus)
# outout = vectorizer.get_feature_names_out()
# array(['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third',
#        'this'], ...)

# (4, 9)


"""
this function is used to get the content- feature_extraction.text
model: CountVectorizer, TfidfTransformer
input: raw content in the table
output: array - which we can used to count how many words in the sentence are related to the topic I'm interested in
"""

# from sklearn.feature_extraction.text import CountVectorizer
#
# df = pd.read_csv("ALL_for_relvscore.csv")
#
# fakew = 'facial recognition facial-recognition faceID ID user innovation innovative cyber cyberspace digit digital digits digitalized artificial intelligence AI ML clone machine learning biometrics security ban bigdata data security privacy personal information private FTC technology tech surveillance camera police crime terrorism computer software system photo identification regulation government legal legislation illegal policy public safe safety detect detects detection bias gender racial racism racist moral law enforcement protection protect systemicracism access control finger bio biological'
#
# lst = []
# for elem in df['text']:
#
#     corpus = [elem, fakew]
#     vectorizer = CountVectorizer()
#     X = vectorizer.fit_transform(corpus)
#     get_feature = vectorizer.get_feature_names_out()
#     count = X.toarray()
#     tot_a = count[0]
#     tot_perfect = count[1]
#     numone = np.count_nonzero(tot_a)
#     numtwo = len(tot_perfect) - np.count_nonzero(tot_perfect)
#     numtotal = numone - numtwo
#     lenofsen = len(elem.split())
#     numfinal = str(float(numtotal / lenofsen))
#     lst.append(numfinal)
#     # print(count)
#
# # fake = 'faceid artificial intelligence machine recognition learning'
#
#
# # print(count)
#
# # lenofsen = len(a) - a.count(" ")
#
# # print(numone)
# # print(numtwo)
# # print(numtotal)
# # print(lenofsen)
# df['sklearn'] = lst
# # print(lst)
# forskl = df[['author_id', 'created_at', 'text', 'YM','nltk_sentiment','bert_sentiment','sklearn']]
#
# updskl = forskl[forskl["sklearn"].str.contains("0.0") == False]
#
# # print(updskl)
#
# updskl.to_csv('ALL_sklearn.csv', index=False)
# print(updskl)
# # print(X.toarray())

"""
this function is used to get the content- feature_extraction.text
input: ALL_sklearn.csv
output: the csv table with the keywords related to government
"""
# from sklearn.feature_extraction.text import CountVectorizer
#
# df = pd.read_csv("ALL_sklearn.csv")
#
# govword = "Police government nationwidesystem mass crowd Communist suspected children crime terrorism surveillance monitor monitoring authority authorities authorization authentication NYPD LAPD securities state Olympics transportation suspect suspects criminals airport Airport city State City border policing anti-surveillance arrest arrests shelter army military homeland terror shooting shootings subway nation national nationwide country countrywide immigration immigrant"
# lst = []
#
# for elem in df['text']:
#
#     corpus = [elem, govword]
#     vectorizer = CountVectorizer()
#     X = vectorizer.fit_transform(corpus)
#     get_feature = vectorizer.get_feature_names_out()
#     count = X.toarray()
#     tot_a = count[0]
#     tot_perfect = count[1]
#     numone = np.count_nonzero(tot_a)
#     numtwo = len(tot_perfect) - np.count_nonzero(tot_perfect)
#     numtotal = numone - numtwo
#     lenofsen = len(elem.split())
#     numfinal = str(float(numtotal / lenofsen))
#     lst.append(numfinal)
#
#
# df['sklearn_gov'] = lst
# # print(lst)
# forskl = df[['author_id', 'created_at', 'text', 'YM','nltk_sentiment','bert_sentiment','sklearn','sklearn_gov']]
#
# regex = r'^0.0$'
# updskl = forskl[forskl["sklearn_gov"].str.contains(regex) == False]
#
# # print(updskl)
#
# updskl.to_csv('ALL_sklearn_gov.csv', index=False)
# print(len(updskl))

"""
this function is used to get the content- feature_extraction.text
input: ALL_sklearn.csv
output: the csv table with the keywords related to company
"""
# from sklearn.feature_extraction.text import CountVectorizer
#
# df = pd.read_csv("ALL_sklearn.csv")
#
# compword = "company companies techcompanies techcompany firm firms corporate Corps bank industry Amazon Microsoft Facebook IBM Google engine online ecommerce commercial Apple iphone iPhone Startup startup business Business Samsung Nvidia start-up market marketing profit profitable viewer viewers consumer customer consumers customers user users client clients enterprice employee employees staff worker"
#
# lst = []
#
# for elem in df['text']:
#
#     corpus = [elem, compword]
#     vectorizer = CountVectorizer()
#     X = vectorizer.fit_transform(corpus)
#     get_feature = vectorizer.get_feature_names_out()
#     count = X.toarray()
#     tot_a = count[0]
#     tot_perfect = count[1]
#     numone = np.count_nonzero(tot_a)
#     numtwo = len(tot_perfect) - np.count_nonzero(tot_perfect)
#     numtotal = numone - numtwo
#     lenofsen = len(elem.split())
#     numfinal = str(float(numtotal / lenofsen))
#     lst.append(numfinal)
#
#
# df['sklearn_comp'] = lst
# # print(lst)
# forskl = df[['author_id', 'created_at', 'text', 'YM','nltk_sentiment','bert_sentiment','sklearn','sklearn_comp']]
#
# regex = r'^0.0$'
# updskl = forskl[forskl["sklearn_comp"].str.contains(regex) == False]
#
# # print(updskl)
#
# updskl.to_csv('ALL_sklearn_comp.csv', index=False)
# print(len(updskl))


"""
this function will be used as an exmaple of processing TF-IDF in the paper
"""
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# form the fake tweet sentence and fake keyword X_package
fake_sentence = "fancy bye faceid"
X_package = "artificial intelligence machine recognition learning faceid"
# plug in the relevant scoring model
corpus = [X_package, fake_sentence]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
get_feature = vectorizer.get_feature_names_out()
# generate score (0 or 1) of each word in the sentence in an array
count = X.toarray()
# get all of the 0s from fake_sentence; all of the 1s from X_package
num_from_sentence = count[0]
num_from_X = count[1]
# count the number of 0s from fake_sentence
total_from_sentence = np.count_nonzero(num_from_sentence)
# since we only care about the valid words which exist in X also in sentence
total_from_X = len(num_from_X) - np.count_nonzero(num_from_X)
valid_total = total_from_sentence - total_from_X
# to get the proportion of valid words in the sentence
length_fake_sentence = len(fake_sentence.split())
final_outcome = str(float(valid_total / length_fake_sentence))

print(final_outcome)


if __name__ == '__main__':
    # print(pairwise_distances(Z, metric='cityblock'))
    # print(X.shape)
    pass
