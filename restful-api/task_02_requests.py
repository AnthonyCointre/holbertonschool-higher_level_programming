#!/usr/bin/python3
"""
Utilize the requests library to send HTTP requests and process responses.
Parse and manipulate JSON data using Python.
Convert structured data into other formats, e.g., CSV.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from a placeholder API and prints their titles.
    """

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    success_code = response.status_code
    print("Status Code: {}".format(success_code))

    if success_code == 200:
        data = response.json()
        for item in data:
            print(item["title"])


def fetch_and_save_posts():
    """
    Fetches posts from a placeholder API and saves them to a CSV file.
    """

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    success_code = response.status_code

    results = []

    if success_code == 200:
        data = response.json()

        for item in data:
            item_dict = {}

            for key, value in item.items():
                item_dict["id"] = item.get("id")
                item_dict["title"] = item.get("title")
                item_dict["body"] = item.get("body")
            results.append(item_dict)

        with open("posts.csv", "w") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
