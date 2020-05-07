#!/usr/bin/python3
""" using the reddit api, returns info about subscribers """
import requests


def number_of_subscribers(subreddit):
    """ returns number of subscribers """

    headers = {'user-agent': 'X-Modhash'}
    url = 'https://www.reddit.com/r/'
    r = requests.get(url + '{}/about.json'.format(subreddit), headers=headers)
    subs = r.json()
    data_subs = subs['data']['subscribers']
    if data_subs is None:
        return 0
    else:
        return data_subs
