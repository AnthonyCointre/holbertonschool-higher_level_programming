#!/usr/bin/python3
"""
Construct a FlyingFish class that inherits
from both a Fish class and a Bird class.
Within FlyingFish, override methods from both parents.
The goal is to comprehend multiple inheritance
and how Python determines method resolution order.
"""


class Fish:
    """
    A class Fish representing a fish with basic behaviors.
    """

    def swim(self):
        """
        Prints a message indicating that the fish is swimming.
        """

        print("The fish is swimming")

    def habitat(self):
        """
        Prints a message indicating the typical habitat of a fish.
        """

        print("The fish lives in water")


class Bird:

    """
    A class Bird representing a bird with basic behaviors.
    """

    def fly(self):
        """
        Prints a message indicating that the bird is flying.
        """

        print("The bird is flying")

    def habitat(self):
        """
        Prints a message indicating the typical habitat of a bird.
        """

        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):

    """
    A class FlyingFish that inherits from both Fish and Bird classes.
    """

    def fly(self):
        """
        Prints a message indicating that the flying fish is soaring.
        """

        print("The flying fish is soaring!")

    def swim(self):
        """
        Prints a message indicating that the flying fish is swimming.
        """

        print("The flying fish is swimming!")

    def habitat(self):
        """
        Prints a message indicating the dual habitat of a flying fish.
        """

        print("The flying fish lives both in water and the sky!")
