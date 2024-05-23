#!/usr/bin/python3
"""
A class Square that inherits from Rectangle (9-rectangle.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a size.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """

        return "[Square] {}/{}".format(self.width, self.height)

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        """

        self.width = value
        self.height = value

    def area(self):
        """
        Calculate the area of the square.
        """

        return self.width ** 2
