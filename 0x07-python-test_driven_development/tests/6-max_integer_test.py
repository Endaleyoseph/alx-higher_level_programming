#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case for max_integer funtion
    using test_max_integer method"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)
        self.assertEqual(max_integer([1, 2, 3, -5]), 3)
        self.assertEqual(max_integer([1, 2, 7, 3]), 7)
        self.assertEqual(max_integer([]), None)
