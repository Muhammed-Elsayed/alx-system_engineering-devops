#!/usr/bin/python3
"""retrieving the top ten hot posts title reddit"""
import requests


def top_ten(subreddit):
    """retreiving the top ten hot posts"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mymachine/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        json_response = response.json()
        for item in json_response['data']['children']:
            print(item['data']['title'])
    else:
        print(None)
