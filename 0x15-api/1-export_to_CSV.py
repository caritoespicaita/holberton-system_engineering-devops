#!/usr/bin/python3
"""  using REST API, export data in csv format
"""
import requests
import sys
import csv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos").json()

    list = []
    with open('{}.csv'.format(sys.argv[1]), 'w') as file:
        cwriter = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=';')
        for task in todos:
            if task.get("userId") == int(sys.argv[1]):
                list = [user.get("id"), user.get("username"),
                        task.get("completed"), task.get("title")]
                cwriter.writerow(list)
