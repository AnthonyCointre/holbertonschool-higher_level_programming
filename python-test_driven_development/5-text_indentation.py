#!/usr/bin/python3
"""
Module to prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function to prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    for char in text:
        result += char

        if char in ".?:":
            result += "\n\n"

    lines = result.split("\n")
    cleaned_lines = [line.strip() for line in lines]
    final_result = "\n".join(cleaned_lines)
    print(final_result)
