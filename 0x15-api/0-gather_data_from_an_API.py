#!/usr/bin/python3
"""
Fetch data from REST API with requests.
"""

from sys import argv
import requests

base_url = "https://jsonplaceholder.typicode.com/users/"
response = requests.get(base_url + argv[1])


def get_employee_data(employee_id):
    """Get data for an employee."""
    response = requests.get(base_url + employee_id)
    return response.json()


employee_data = get_employee_data(argv[1])
employee_name = employee_data["name"]

todos_data = requests.get(base_url + argv[1] + "/todos").json()

titles_list = []

for task in todos_data:
    if task.get('completed') is True:
        titles_list.append(task.get('title'))

print(f"Employee {employee_name}
      tasks({len(titles_list)}/{len(todos_data)}): ")

for title in titles_list:
    print(f"\t{title}")
