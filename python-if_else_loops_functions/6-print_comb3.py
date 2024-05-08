#!/usr/bin/python3
for tens in range(0, 9):
    for units in range((tens + 1), 10):
        if tens == 8 and units == 9:
            print("{}".format(89))
        else:
            print("{}{}, ".format(tens, units), end="")
