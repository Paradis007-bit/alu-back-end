#!/usr/bin/python3
"""0-gather_data_from_an_API.py
Fetches an employee's TODO list and prints their progress
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    emp_id = sys.argv[1]

    # Fetch user data
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    user_res = requests.get(user_url).json()
    username = user_res.get("username")

    # Fetch TODOs
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
    todos = requests.get(todos_url).json()

    total_tasks = len(todos)
    done_tasks = sum(1 for task in todos if task.get("completed"))

    # Print summary line with colon
    print("Employee {} is done with tasks({}/{}):".format(username, done_tasks, total_tasks))

    # Print completed tasks titles, each preceded by a tab and a space
    for task in todos:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
