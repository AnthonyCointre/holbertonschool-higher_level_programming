#!/usr/bin/python3
"""
Create a class named VerboseList that extends the Python list class.
This custom class should print a notification message every time an item
is added (using the append or extend methods)
or removed (using the remove or pop methods).
"""


class VerboseList(list):
    """
    class VerboseList that inherits from the built-in list class.
    """

    def append(self, object):
        """
        Adds an item to the end of the list and prints a notification message.
        """
        super().append(object)

        print(f"Added [{object}] to the list.")

    def extend(self, iterable):
        """
        Extends the list by appending elements from the iterable and prints
        a notification message.
        """

        super().extend(iterable)

        num_items = 0

        for item in iterable:
            num_items = num_items + 1

        print(f"Extended the list with [{num_items}] items.")

    def remove(self, value):
        """
        Removes the first occurrence of the value from the list and prints
        a notification message.
        """

        super().remove(value)

        print(f"Removed [{value}] from the list.")

    def pop(self, index=-1):
        """
        Removes and returns the item at the specified index from the list
        and prints a notification message.
        """

        item = super().pop(index)

        print(f"Popped [{item}] from the list.")

        return item
