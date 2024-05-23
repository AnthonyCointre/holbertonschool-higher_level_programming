#!/usr/bin/python3
"""
A class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.
        """

        self._size = size
        super().integer_validator("size", size)
        super().integer_validator("size", size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """

        r = "[Square]"
        return (f"{r} {self._size}/{self._size}")

    def area(self):
        """
        Computes the area of the square.
        """

        area = self._size * self._size
        return area
