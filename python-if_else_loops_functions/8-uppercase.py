#!/usr/bin/python3
def uppercase(string):
    result = ""
    for character in string:
        if 97 <= ord(character) <= 122:
            result += chr(ord(character) - 32)
        else:
            result += chr(ord(character))
    print("{}".format(result))
