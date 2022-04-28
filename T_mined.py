"""
Created on 1/25/22

@author: qinyuzhu
"""
import json

import requests
import csv
import time

bearer_token = "AAAAAAAAAAAAAAAAAAAAAIYNYQEAAAAAeT2fIGZnTTN58tY1UmIHXDupsoU%3DyK6fGHNrhxUA0DCJvxkZX26c4WZ3F3L0n0bpk8reHmv6V7wbYr"

def create_url():
    """
    this function is used to include the user_fields
    and the url/id for the retweet
    return the customized information I want from that tweet
    """
    count = 500
    url = "https://api.twitter.com/2/tweets/search/all"
    keywords = "#facialrecognition OR #FacialRecognition OR #FacialRecognitionSoftware OR #FacialID"
    # keywords = "(@washingtonpost is:rewteet) (facialrecognition)"
    start_time = '2019-12-31T01:01:00Z'
    end_time = '2019-12-31T23:59:59Z'

    query_params = {'query': keywords,
                    'tweet.fields': 'created_at,lang',
                    'max_results': count,
                    'start_time': start_time,
                    'end_time': end_time,
                    "user.fields": "verified,withheld,public_metrics",
                    "place.fields":"country_code",
                    'expansions': 'author_id',
                    'next_token': {}}
    return url,query_params


def bearer_oauth(r):
    """
    for bearer token authentication
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_endpoint(url, query_params):
    response = requests.get(url, auth=bearer_oauth, params=query_params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
    return response.json()


def main():
    url, query_params = create_url()
    json_response = connect_endpoint(url, query_params)
    json_data = json.dumps(json_response, indent=4, sort_keys=True)
    print(json_data)

    with open('try_1912.json','w') as file:
        json.dump(json_data,file)

    with open('try_1912.json') as f:
        js = json.load(f)
        js_updated = json.loads(js)

    csv_columns = ['author_id', 'created_at', 'id', 'lang', 'text']
    csv_file = 'out_1912.csv'
    try:
        with open(csv_file, 'a', newline='') as csvfile:
            dictwriter_object = csv.DictWriter(csvfile, fieldnames=csv_columns)
            # Pass the data in the dictionary as an argument into the writerow() function

            # writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            # writer.writeheader()
            for data in js_updated["data"]:
                # writer.writerow(data)
                dictwriter_object.writerow(data)
                # print(data)
    except IOError:
        print("I/O error")

if __name__ == '__main__':

    main()
    start_time = time.time()
    # print("--- %s seconds ---" % (time.time() - start_time))
