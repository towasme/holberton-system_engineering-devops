#!/usr/bin/python3
""" using the reddit api, returns info about first ten titles """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ top ten titles in subreddit """
    headers = {'user-agent': 'X-Modhash'}
    limit = {"limit": 100}
    if after is not None:
        limit['after'] = after
    url = 'https://www.reddit.com/r/'
    status = requests.get(url + '{}/hot.json'.format(subreddit),
                          headers=headers, params=limit)
    subs = status.json()
    if status.status_code is 200:
        for i in range(len(subs['data']['children'])):
            hot_list.append(subs['data']['children'][i]['data']['title'])
        if subs['data']['after'] is not None:
            recurse(subreddit, hot_list, subs['data']['after'])
        return hot_list
    else:
        return None
