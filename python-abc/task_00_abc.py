#!/usr/bin/python3
"""
An abstract class named Animal using the ABC package.
This class should have an abstract method called sound.

Two subclasses of Animal: Dog and Cat.
Implement the sound method in each subclass to return
the strings “Bark” and “Meow” respectively.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class Animal using the ABC module
    to create abstract methods.
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    A class Dog that inherits from Animal and implements the sound method.
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    A class Cat that inherits from Animal and implements the sound method.
    """

    def sound(self):
        return "Meow"
