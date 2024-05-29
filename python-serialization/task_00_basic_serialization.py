#!/usr/bin/python3*
"""
A basic serialization module that adds the functionality to serialize
a Python dictionary to a JSON file and deserialize the JSON file
to recreate the Python Dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Deserialize a JSON file and recreate Python dictionary.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return (json.load(file))
