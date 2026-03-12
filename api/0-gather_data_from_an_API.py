#!/usr/bin/python3
"""Gather an employee's TODO list progress from JSONPlaceholder API."""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    emp_id = sys.argv[1]

    # Fetch employee data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    user_res = requests.get(user_url).json()
    emp_name = user_res.get("name")

    # Fetch employee's todos
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
    todos = requests.get(todos_url).json()

    total_tasks = len(todos)
    done_tasks = [task["title"] for task in todos if task["completed"]]

    # Output progress
    print("Employee {} is done with tasks({}/{}):".format(emp_name, len(done_tasks), total_tasks))
    for title in done_tasks:
        print("\t {}".format(title))
