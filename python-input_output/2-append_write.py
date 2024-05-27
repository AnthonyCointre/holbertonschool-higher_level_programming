#!/usr/bin/python3

"""
A string at the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    A string at the end of a text file (UTF8)
    and returns the number of characters added.
    """

    with open(filename, mode="a", encoding="utf-8") as file:
        nb_characters_added = file.write(text)
        return (len(text))
