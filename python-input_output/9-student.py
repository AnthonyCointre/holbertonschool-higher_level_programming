#!/usr/bin/python3
"""
A class Student that defines a student by:

Public instance attributes:
first_name
last_name
age
"""


class Student():
    """
    A class Student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize the Student object.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """
        Method that returns the dictionary representation
        of a Student instance.
        """

        return (self.__dict__)
