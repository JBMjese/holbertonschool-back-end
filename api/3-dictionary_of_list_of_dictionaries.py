#!/usr/bin/python3
"""Script to use a REST API to export data in JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"

    response = requests.get(f"{API_URL}/users")
    users = response.json()

    all_employees = {}

    for user in users:
        user_id = user["id"]
        response = requests.get(
            f"{API_URL}/users/{user_id}/todos",
            params={"_expand": "user"}
        )
        tasks = response.json()

        user_tasks = []
        for task in tasks:
            task_dict = {
                "username": task["user"]["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            user_tasks.append(task_dict)

        all_employees[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as file:
        json.dump(all_employees, file)
