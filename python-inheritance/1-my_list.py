#!/usr/bin/python3
"""
A class MyList that inherits from list.
"""


class MyList(list):
    """
    A class MyList.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """

        print(sorted(self))
