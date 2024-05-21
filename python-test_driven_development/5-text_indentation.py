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
    i = 0

    while i < len(text):
        print(text[i], end='')
        if text[i] in chars_to_indent:
            print('\n')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
