#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""


class BaseGeometry:
    """
    A class BaseGeometry.
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
