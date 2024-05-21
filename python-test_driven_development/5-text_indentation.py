#!/usr/bin/python3
"""
Module to prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function to print a text with 2 new lines
    after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars_to_indent = ['.', '?', ':']

    for i, char in enumerate(text):
        print(char, end='')
        if char in chars_to_indent:
            if i + 1 < len(text) and text[i + 1] != ' ':
                print('\n\n', end='')

            else:
                print('\n', end='')
