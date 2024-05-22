#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Define the base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch a list of all users from the API
    users = requests.get(url + "users").json()

    # Open a JSON file for writing
    with open("todo_all_employees.json", "w") as jsonfile:
        # Use json.dump to write a JSON object to the file
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(
                url + "todos", params={
                    "userId": u.get("id")
                    }).json()]
            for u in users
        }, jsonfile)
