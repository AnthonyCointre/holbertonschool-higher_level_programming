#!/usr/bin/python3
def uppercase(string):
    for character in string:
        if 97 <= ord(character) <= 122:
            print(chr(ord(character) - 32), end='')
        else:
            print(character, end='')
    print()
