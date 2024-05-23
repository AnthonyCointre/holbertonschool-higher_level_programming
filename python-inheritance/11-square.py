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

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square.
        """

        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Calculate the area of the square.
        """

        return self.__size ** 2
