#!/usr/bin/python3
"""Script that gathers data from the JSONPlaceholder API for a given employee ID
and displays their TODO list progress.
"""

import requests
import sys


def main():
    """Fetches employee info and TODO list from API and prints completed tasks."""
    if len(sys.argv) != 2:
        return

    employee_id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user = requests.get(url_user).json()
    todos = requests.get(url_todos).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task.get("title") for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(done_tasks), total_tasks))
    for title in done_tasks:
        print("\t {}".format(title))


if __name__ == "__main__":
    main()
