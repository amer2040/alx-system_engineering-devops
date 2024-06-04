#!/usr/bin/python3
""" function that returns the number of subscribers """

import requests

def number_of_subscribers(subreddit):
    """If not a valid subreddit, return 0
       or returns the number of subscribers
    """
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    headers = {'User-Agent': 'reconnect/1.0'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    else:
        return res.json().get('data').get('subscribers')
