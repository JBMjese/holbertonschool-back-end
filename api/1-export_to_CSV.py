#!/usr/bin/python3
"""
Script to retrieve and export TODO list progress for a given employee ID
using a REST API.
"""

import json
import requests
import sys


def export_list(employee_id):
    """
    Retrieve TODO list progress for a given employee.
    """
    API_URL = "https://jsonplaceholder.typicode.com"
    response = requests.get(
        f"{API_URL}/users/{employee_id}/todos",
        params={"_expand": "user"}
    )
    data = response.json()

    if not len(data):
        print("RequestError:", 404)
        sys.exit(1)

    employee_name = data[0]["user"]["name"]
    tasks = []
    for task in data:
        tasks.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        })

    json_data = {employee_id: tasks}

    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_list(employee_id)
