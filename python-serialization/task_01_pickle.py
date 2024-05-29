#!/usr/bin/python3
"""
Serialize and deserialize custom Python objects using the pickle module.
"""

import pickle


class CustomObject:
    """
    A class CustomObject.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize CustomObject.
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print object attributes.
        """

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize.
        """

        try:
            with open(filename, mode="wb") as file:
                pickle.dump(self, file)
        except Exception:
            return (None)

    @classmethod
    def deserialize(cls, filename):
        """
        A class method deserialize.
        """

        try:
            with open(filename, mode="rb") as file:
                return (pickle.load(file))
        except Exception:
            return (None)
