#!/usr/bin/python3
"""fetching some data using rest api using python and request library"""
import csv
import requests
from sys import argv


def display():
    """display function"""
    link = "https://jsonplaceholder.typicode.com/users/"

    response = requests.get(link + argv[1])
    # get the employee name in json
    employee_name = response.json().get("username")
    # get all the tasks data in json format
    todos_response_json = requests.get(link + argv[1] + "/todos").json()

    file_name = "{}.csv".format(argv[1])

    tasks = []
    for task in todos_response_json:
        data = [
            argv[1],
            employee_name,
            task.get('completed'),
            task.get('title')
        ]
        tasks.append(data)

    with open(file_name, "w") as new_file:
        csv_writer = csv.writer(new_file, quoting=csv.QUOTE_ALL)
        for value in tasks:
            csv_writer.writerow(value)


if __name__ == "__main__":
    display()
