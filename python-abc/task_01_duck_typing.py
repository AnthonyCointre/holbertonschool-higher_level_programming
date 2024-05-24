#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
"""
Create an abstract class named Shape with two abstract methods:
area and perimeter.

Implement two concrete classes: Circle and Rectangle,
both inheriting from Shape.
Each class should provide implementations for the area and perimeter methods.

Write a standalone function named shape_info that accepts an object of
type Shape (by duck typing) and prints its area and perimeter.

Test the shape_info function with instances of both Circle and Rectangle.
"""


class Shape(ABC):
    """
    Abstract class Shape using the ABC module to create abstract
    methods.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method that should be implemented by all subclasses of Shape.
        """

        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method that should be implemented by all subclasses of Shape.
        """

        pass


class Circle(Shape):
    """
    A class Circle that inherits from Shape and implements the area
    and perimeter methods.
    """

    def __init__(self, radius):
        """
        Initializes a Circle object with the specified radius.
        """

        self.radius = radius

    def area(self):
        """
        Implements the area method for Circle.
        """

        area = pi * ((self.radius) ** 2)
        return area

    def perimeter(self):
        """
        Implements the perimeter method for Circle.
        """

        perimeter = 2 * pi * (abs(self.radius))
        return perimeter


class Rectangle(Shape):
    """
    A class Rectangle that inherits from Shape and implements the area
    and perimeter methods.
    """

    def __init__(self, height=0, width=0):
        """
        Initializes a Rectangle object with the specified height and width.
        """

        self.height = height
        self.width = width

    def area(self):
        """
        Implements the area method for Rectangle.
        """

        area = self.height * self.width
        return area

    def perimeter(self):
        """
        Implements the perimeter method for Rectangle.
        """

        perimeter = (2 * self.height) + (2 * self.width)
        return perimeter


def shape_info(shape):
    """
    Standalone function to print out the area and perimeter of a given shape.
    """

    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
