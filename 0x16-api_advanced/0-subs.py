#!/usr/bin/python3
""" using the reddit api, returns info about subscribers """
import requests


def number_of_subscribers(subreddit):
    """ returns number of subscribers """
    headers = {'user-agent': 'X-Modhash'}
    url = 'https://www.reddit.com/r/'
    r = requests.get(url + '{}/about.json'.format(subreddit), headers=headers)
    subs = r.json()
    try:
        data_subs = subs['data']['subscribers']
        return data_subs
    except:
        return 0
