#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 0-rectangle.py).
"""

Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
