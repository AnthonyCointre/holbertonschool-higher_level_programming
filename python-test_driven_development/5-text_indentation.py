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

    chars_to_indent = ['.', '?', ':']

    for char in text:
        print(char, end='')

        if char in chars_to_indent:
            print('\n\n', end='')
