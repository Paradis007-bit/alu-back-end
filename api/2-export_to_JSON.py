#!/usr/bin/python3
"""Export employee TODO list to JSON file for a given employee ID."""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage = "Usage: {} <employee_id>".format(sys.argv[0])
        print(usage)
        sys.exit(1)

    emp_id = sys.argv[1]

    # Fetch user data
    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    )
    user_res = requests.get(user_url).json()
    username = user_res.get("username")

    # Fetch TODOs
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(emp_id)
    )
    todos = requests.get(todos_url).json()

    # Prepare JSON data
    json_data = {emp_id: []}
    for task in todos:
        json_data[emp_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    # Write to JSON file
    filename = "{}.json".format(emp_id)
    with open(filename, mode="w") as json_file:
        json.dump(json_data, json_file)
