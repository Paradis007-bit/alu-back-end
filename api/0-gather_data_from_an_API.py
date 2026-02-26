#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress
from a REST API.
"""

import requests
import sys


def main():
    """
    Main function that retrieves and prints
    the TODO list progress for a given employee ID.
    """
    if len(sys.argv) != 2:
        return

    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        return

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")

    employee_tasks = [
        task for task in todos if task.get("userId") == int(employee_id)
    ]

    completed_tasks = [
        task for task in employee_tasks if task.get("completed") is True
    ]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            len(completed_tasks),
            len(employee_tasks)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
