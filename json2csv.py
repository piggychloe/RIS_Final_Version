"""
Created on 3/8/22

@author: qinyuzhu
"""
import requests
import os
import pandas as pd
import pyreadstat
import json
import csv
import pickle


with open('get_1801.json') as f:
    js = json.load(f)
    js_updated = json.loads(js)


    # print(js_updated['includes'])
    # print(js_updated['data'][0])
    # print(js_updated['data'][0]['text'])
    # print(js_updated.head())

"""
use to convert the json file to csv
"""
csv_columns = ['author_id','created_at','id','lang','text']
csv_file = 'trans_1801.csv'
try:
    with open(csv_file,'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        # for data in js_updated:
        #     data = js_updated["data"]
        #     for info in data:
        #         writer.writerow(data)
        #         print(info)
        for data in js_updated["data"]:
            writer.writerow(data)
            print(data)
except IOError:
    print("I/O error")

"""
use to read specific line in the csv file
"""
# col_list = ['lang']
# data = pd.read_csv(r'smlSAMPLE_1912.csv',usecols=col_list)
# csv_file = 'smlSAMPLE_1912.csv'

"""
use to read the csv file
"""
# data = pd.read_csv("smlSAMPLE_1912.csv")
# for i in range(0,500):
#     if data['text'][i]:
#         print(data['text'].iloc[i])

'''
with open(r'data_senator_xmas_final.csv') as f:
    csv_data = csv.reader(f, delimiter=',')
    data = [row for row in csv_data]

df = pd.DataFrame(data[1:], columns=data[0])
print(df.head())
'''




# df = pd.read_spss("ATP.sav")
# dpy = pyreadstat.read_sav("ATP.sav")

# f = open("Twitter API v2.postman_environment.json")
# f_f = open("Twitter API v2.postman_collection.json")

# df = pd.read_json('data_senator.json', orient='index')
# csvData = df.to_csv ('data_senator.csv', index = False)

# with open('data_senator.json') as f:
#     json_data = json.load(f)
#
# with open('data_senator_two.csv','w') as f:
#     df = pd.DataFrame(json_data)
#     df.to_csv('data_senator_two.csv', index=False)
#     result = pd.read_csv('data_senator_two.csv')

# with open("samplecsv.csv", 'w') as f:
#     wr = csv.DictWriter(f, fieldnames = info[0].keys())
#     wr.writeheader()
#     wr.writerows(info)
#
# with open("data_senator_new.json","r") as f:
#     my_data = json.load(f)
# json_df = pd.read_json(my_data)

if __name__ == '__main__':
    pass
