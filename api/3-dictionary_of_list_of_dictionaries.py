#!/usr/bin/python3
"""Exports all employees' tasks to a JSON file."""

import json
import requests

if __name__ == "__main__":
    # Get all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url).json()

    # Get all todos
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(todos_url).json()

    # Create dictionary of lists
    all_data = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        all_data[user_id] = [
            {"username": username,
             "task": task.get("title"),
             "completed": task.get("completed")}
            for task in todos if task.get("userId") == user.get("id")
        ]

    # Write to JSON file
    with open("todo_all_employees.json", "w") as f:
        json.dump(all_data, f)
