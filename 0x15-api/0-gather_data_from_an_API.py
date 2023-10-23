#!/usr/bin/python3
"""A Python script that, using this REST API, for a given employee ID."""

import requests
from sys import argv


# link to get the data
link = "https://jsonplaceholder.typicode.com/users/"

# request the data for certain user
response = requests.get(link + argv[1])

# convert data into json
json_data = response.json()

employee_name = json_data["name"]

# request todos data for one user
todos_response = requests.get(link + argv[1] + "/todos")

# convert data into json
todos_response_json = todos_response.json()


# getting the number of tasks and the title of it
titles_ls = []
for task in todos_response_json:
    if (task.get('completed') is True):
        titles_ls.append(task.get('title'))


print("Employee {}is done with tasks({}/{}): "
      .format(employee_name, len(titles_ls), len(todos_response_json)))

for title in titles_ls:
    print("\t {}".format(title))
