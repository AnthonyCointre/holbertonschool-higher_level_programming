#!/usr/bin/python3
"""
Unittests for the function def max_integer(list=[]):.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_only_one(self):
        self.assertEqual(max_integer([1]), 1)

    def test_max_begin(self):
        self.assertEqual(max_integer([4, 3, 2]), 4)

    def test_max_mid(self):
        self.assertEqual(max_integer([3, 4, 2]), 4)

    def test_max_end(self):
        self.assertEqual(max_integer([2, 3, 4]), 4)

    def test_max_one_is_negative(self):
        self.assertEqual(max_integer([2, -3, 4]), 4)

    def test_max_all_are_negative(self):
        self.assertEqual(max_integer([-2, -3, -4]), -2)


if __name__ == '__main__':
    unittest.main()
