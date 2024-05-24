#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
Create an abstract class named Animal using the ABC package.
This class should have an abstract method called sound.

Create two subclasses of Animal: Dog and Cat.
Implement the sound method in each subclass to return
the strings “Bark” and “Meow” respectively.
"""


class Animal(ABC):
    """
    Abstract class Animal using the ABC module
    to create abstract methods.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by all subclasses of Animal.
        """

        pass


class Dog(Animal):
    """
    A class Dog that inherits from Animal and implements the sound method.
    """

    def sound(self):
        """
        Implements the sound method for Dog.
        """

        return "Bark"


class Cat(Animal):
    """
    A class Cat that inherits from Animal and implements the sound method.
    """

    def sound(self):
        """
        Implements the sound method for Cat.
        """

        return "Meow"
