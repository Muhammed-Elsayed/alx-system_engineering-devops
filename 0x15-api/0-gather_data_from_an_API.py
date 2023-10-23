#!/usr/bin/python3
"""fetching some data using rest api using python and request library"""
import requests
from sys import argv


def display():
    """display function"""
    link = "https://jsonplaceholder.typicode.com/users/"

    response = requests.get(link + argv[1])

    json_data = response.json()

    employee_name = json_data["name"]

    todos_response = requests.get(link + argv[1] + "/todos")

    todos_response_json = todos_response.json()

    titles_ls = []
    for task in todos_response_json:
        if (task.get('completed') is True):
            titles_ls.append(task.get('title'))

    print("Employee {} is done with tasks ({}/{}): "
          .format(employee_name, len(titles_ls), len(todos_response_json)))

    for title in titles_ls:
        print("\t {}".format(title))


if __name__ == "__main__":
    display()
