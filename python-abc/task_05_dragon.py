#!/usr/bin/python3
"""
Design two mixin classes, SwimMixin and FlyMixin,
each equipped with methods swim and fly respectively.
Next, construct a class Dragon that inherits from both these mixins.
Your aim is to show that a Dragon instance can both swim and fly.
"""


class SwimMixin:
    """
    A class SwimMixin provides a swimming ability
    to any class that inherits from it.
    """

    def swim(self):
        """
        Prints a message indicating that the creature can swim.
        """

        print("The creature swims!")


class FlyMixin:
    """
    A class FlyMixin provides a flying ability
    to any class that inherits from it.
    """

    def fly(self):
        """
        Prints a message indicating that the creature can fly.
        """

        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class Dragon that inherits from both SwimMixin and FlyMixin,
    indicating that a dragon can both swim and fly.
    """

    def roar(self):
        """
        Prints a message indicating that the dragon can roar.
        """

        print("The dragon roars!")
