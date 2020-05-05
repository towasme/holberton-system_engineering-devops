#!/usr/bin/python3
""" using the rest api, returns info about someone """
import sys
import urllib.request


if __name__ == "__main__":
    url = ('https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    with urllib.request.urlopen(url) as response:
        print(response.getheader('name'))
