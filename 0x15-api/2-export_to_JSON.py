#!/usr/bin/python3
"""
Script that exports TODO list data for a given employee ID to a JSON file.
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user data
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    ).json()

    # Fetch TODO list
    todo_data = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(employee_id)
    ).json()

    # Create JSON file
    json_filename = '{}.json'.format(employee_id)

    data_to_export = {
        str(user_data['id']): [{"task": task['title'],
                                "completed": task['completed'],
                                "username": user_data['username']
                                } for task in todo_data]
        }

    with open(json_filename, 'w') as json_file:
        json.dump(data_to_export, json_file)

    print("Data exported to {}".format(json_filename))
