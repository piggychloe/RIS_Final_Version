"""
Created on 3/25/22

@author: qinyuzhu
"""
import pandas as pd
import numpy as np
import nltk
from csv import reader
from csv import writer
from nltk.corpus import stopwords

"""
intro: this function is used to get the average of sentiment for 24 months
hue: nltk_only; bert_only; union; intersection;
period: all YM
column: months; sentiment; 
"""
df = pd.read_csv("combine_togo.csv")


if __name__ == '__main__':
    pass
