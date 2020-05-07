#!/usr/bin/python3
""" using the reddit api, returns info about first ten titles """
import requests


def top_ten(subreddit):
    """ top ten titles in subreddit """
    headers = {'user-agent': 'X-Modhash'}
    url = 'https://www.reddit.com/r/'
    r = requests.get(url + '{}/.json'.format(subreddit), headers=headers)
    subs = r.json()
    subs_data = subs['data']
    data_children = subs_data['children']
    for i in range(10):
        print(data_children[i]['data']['title'])
    return
