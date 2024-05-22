#!/usr/bin/python3
"""
Script that exports TODO list data for a given employee ID to a CSV file.
"""

import csv
import requests
import sys

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Retrieve user ID from command line arguments
    user_id = sys.argv[1]

    # Define the base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user details using the provided user ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch TODO list for the specified user ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Open a CSV file for writing
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Iterate through each TODO item and write a row to the CSV file
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
