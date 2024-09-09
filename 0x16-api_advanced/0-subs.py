#!/usr/bin/python3
"""
This doc for module
"""

import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}

def number_of_subscribers(subreddit):
    """Returns the number of subscribers in a given subreddit."""
    try:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        response = requests.get(url, allow_redirects=False, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data["data"]["subscribers"]
    except (requests.RequestException, KeyError):
        # Handle cases where the request fails or raises an exception
        print(f"An error occurred: {response.status_code}")
        return 0
