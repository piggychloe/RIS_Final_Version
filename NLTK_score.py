"""
Created on 3/9/22

@author: qinyuzhu
"""

from nltk.sentiment import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np
import functools

def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    word = sentiment_dict

    # print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    # print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    # print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

    # print("Sentence Overall Rated As", end=" ")

    if sentiment_dict['compound'] >= 0.05:
        test =  "POSITIVE"

    elif sentiment_dict['compound'] <= - 0.05:
        test = "NEGATIVE"

    else:
        test = "neu"

    return test




if __name__ == '__main__':
    # sentence = "I am good."
    # print(sentiment_scores(sentence))



    # col_list = ['text']
    data = pd.read_csv(r'dwed_1803.csv', engine='python')

    # df = pd.DataFrame(data, columns=['text'])
    # data['score'] = list
    ttt = data['text']
    # print(ttt)
    # print(data)
    ret = []
    for sentence in ttt:
        upd = str(sentence)
        new = sentiment_scores(upd)
        ret.append(new)
        # data['score'] = new

    print(ret)
    data['score'] = ret
    data.to_csv("Ned_1803.csv",index=False)
    # print(data)
    # print(data)
    # print(data)
    # print(data)

        # print(sentence)

    # out = df.apply(lambda x: sentiment_scores(x))
    # print(out)


    # cline = open("labeled_SAMPLE.csv","r")
    # for line in cline:
    #     ret.append(sentiment_scores(line))

    # for i,j in data.iteritems:
    #     print(i,sentiment_scores(j))
    #     # ret.append(sentiment_scores(line))
    # data.close()

    # for k in ret:
    #     print(k)
        # print(len(ret))
        # np.savetxt("smlSAMPLE_sa.txt", ret, delimiter=" ", newline="\n",
        #            fmt="%s")

    # with open(r'MYDATA_test_v7.txt') as f:
    #     for line in f:
    #         print(sentiment_scores(line))
