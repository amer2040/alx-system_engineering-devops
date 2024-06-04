#!/usr/bin/python3
"""function that prints the titles of the first top 10 hot posts listed"""

import requests


def top_ten(subreddit):
    """ print top 10 titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'reconnect/1.0'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        print('None')
    else:
        top10 = res.json().get('data').get('children')
        for x in range(10):
            print(top10[x].get('data').get('title'))
