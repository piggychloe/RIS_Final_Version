"""
Created on 3/9/22

@author: qinyuzhu
"""
import pandas as pd
"""
input: the table with NLTK score appended
output: the table with all rows of non-neutral NLTK score
"""
# df = pd.read_csv("Ned_1912.csv")
# data = df[df["score"].str.contains("neu") == False]
# data.to_csv('Neucleaned_1912.csv', index=False)
# print(data)

if __name__ == '__main__':
    df = pd.read_csv('Neucleaned_1801.csv')
    print(df)
