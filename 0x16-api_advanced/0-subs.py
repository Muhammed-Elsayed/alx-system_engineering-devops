#!/usr/bin/env python3
import requests


def number_of_subscribers(subreddit):
    """retreiving the number of subscribers in a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mymachine/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return (0)

    results = response.json().get('data')
    return (results.get('subscribers'))
