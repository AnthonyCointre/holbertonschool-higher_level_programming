#!/usr/bin/python3
"""
Create a class named CountedIterator that extends
the built-in iteratorobtained from the iter function.
The CountedIterator should keep track of the number
of items that have been iterated over.
Specifically, you will need to override the __next__ method
to increment a counter each time an item is fetched.
"""


class CountedIterator:
    """
    A class CountedIterator that extends the built-in iterator
    obtained from the iter function.
    """

    def __init__(self, iterator, count=0):
        """
        Initializes the CountedIterator with an iterator and an optional
        initial count.
        """

        self.iterator = iter(iterator)
        self.count = count

    def get_count(self):
        """
        Returns the current count of iterated items.
        """

        return self.count

    def __next__(self):
        """
        Returns the next item from the iterator and increments the count.
        """

        item = next(self.iterator)
        if item:
            self.count = self.count + 1
            return item
        else:
            raise StopIteration
