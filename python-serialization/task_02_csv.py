#!/usr/bin/python3
"""
reading data from one format (CSV) and converting it into
another format (JSON) using serialization techniques.
"""

import json
import csv


def convert_csv_to_json(filename):
    """
        Takes the CSV filename as its parameter and writes a JSON file.
    """

    try:
        with open(filename, mode="r", encoding="utf-8") as csv_file:
            csv_data = csv.DictReader(csv_file)
            csv_lines = []
            for lines in csv_data:
                csv_lines.append(lines)

        with open("data.json", mode="w", encoding="utf-8") as json_File:
            json.dump(csv_lines, json_File)
        return (True)

    except FileNotFoundError:
        return (False)
