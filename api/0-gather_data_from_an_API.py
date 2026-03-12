#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

Fetches an employee's TODO list from JSONPlaceholder API and displays progress.
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    emp_id = sys.argv[1]

    # Fetch user data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    user_res = requests.get(user_url).json()
    username = user_res.get("name")  # EMPLOYEE_NAME

    # Fetch TODOs
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
    todos = requests.get(todos_url).json()

    # Count completed tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]

    # First line: Employee progress
    print("Employee {} is done with tasks({}/{})".format(
        username, len(done_tasks), total_tasks))

    # Print completed task titles
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
