#!/usr/bin/python3
"""
Script that retrieves TODO list progress
for a given employee ID from a REST API.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetching user data
    user_data = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                employee_id
                )).json()

    # Fetching TODO list
    todo_data = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                employee_id
                )).json()

    # Counting completed and total tasks
    total_tasks = len(todo_data)
    completed_tasks = sum(task['completed'] for task in todo_data)

    # Displaying results
    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], completed_tasks, total_tasks
        ))
    for task in todo_data:
        if task['completed']:
            print("\t {}".format(task['title']))
