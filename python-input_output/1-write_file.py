#!/usr/bin/python3
"""
A string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    A string to a text file (UTF8)
    and returns the number of characters written.
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        nb_characters = file.write(text)
        return (len(text))
