#!/usr/bin/python3
"""  using REST API
"""
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = []
    titles = []

    for task in todos:
        if task.get("completed") is True:
            completed.append(task.get("completed"))
            titles.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
          user.get("name"), len(completed), len(todos)))
    for title in titles:
        print("\t {}".format(title))
