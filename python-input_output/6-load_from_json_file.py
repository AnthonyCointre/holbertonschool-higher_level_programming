#!/usr/bin/python3
"""
Creates an Object from a “JSON file”.
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.
    """

    with open(filename, mode="r", encoding="utf-8") as file:
        json_str = file.read()
        object = json.loads(json_str)
        return (object)
