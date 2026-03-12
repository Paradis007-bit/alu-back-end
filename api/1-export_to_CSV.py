#!/usr/bin/python3
"""Export employee TODO list to CSV file for a given employee ID."""

import csv
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

    # CSV filename
    filename = "{}.csv".format(emp_id)

    # Write tasks to CSV
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
