#!/usr/bin/python3
""" using the rest api, returns info about someone """
import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    r = requests.get(url + 'users/{}'.format(sys.argv[1]))
    all_users = r.json()
    USERNAME = all_users['username']

    t = requests.get(url + 'todos?userId={}'.format(sys.argv[1])).json()
    USER_ID = t['userId']

    with open("{}.csv".format(USER_ID), "w", newline="") as csv_file:
        csv2write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for dictionary in t:
            title = dictionary['title']
            status = dictionary['completed']
            csv2write.writerow(USER_ID, USERNAME, status, title)
