#!/usr/bin/python3
"""
A class Student that defines a student by: (based on 10-student.py)

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


    def to_json(self, attrs=None):
        """
        Method that returns the dictionary representation
        of a Student instance.
        """

        dictionary = {}

        if isinstance(attrs, list):
            flag = True
        else:
            flag = False

        for key, value in self.__dict__.items():
            if flag:
                for val in attrs:
                    if val == key:
                        dictionary[key] = value
            else:
                dictionary[key] = value

        return (dictionary)


    def reload_from_json(self, json):
        """
        Method that replace all attributes
        of Student instance.
        """

        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
