#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        A class Rectangle that inherits from BaseGeometry.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
