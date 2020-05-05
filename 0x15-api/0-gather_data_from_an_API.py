#!/usr/bin/python3
""" using the rest api, returns info about someone """
import sys
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    r = requests.get(url + 'users/{}'.format(sys.argv[1]))
    all_users = r.json()
    EMPLOYEE_NAME = all_users['name']

    t = requests.get(url + 'todos?userId={}'.format(sys.argv[1])).json()
    c = requests.get(url + 'todos?userId={}&completed=true'
                     .format(sys.argv[1])).json()
    TOTAL_NUMBER_OF_TASKS = len(t)
    NUMBER_OF_DONE_TASKS = len(c)
    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    [print('\t {}'.format(e['title'])) for e in c]
