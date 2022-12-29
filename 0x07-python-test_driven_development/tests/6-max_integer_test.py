#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case for max_integer funtion
    using test_max_integer method"""
    def test_module_docstring(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)
        self.assertEqual(max_integer([1, 2, 3, -5]), 3)
        self.assertEqual(max_integer([1, 2, 7, 3]), 7)
        self.assertEqual(max_integer([]), None)

    def test_max_float(self):
        self.assertEqual(max_integer([1, 2.9, 3, 5.5]), 5.5)
        self.assertEqual(max_integer([{5.5, 1.1}, {4, 0}]), {5.5, 1.1})

    def test_max_strings(self):
        self.assertEqual(max_integer("123456"), "6")
        self.assertEqual(max_integer(""), None)

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            max_integer(45)
        with self.assertRaises(TypeError):
            max_integer([-5, 7, "9"])
        with self.assertRaises(TypeError):
            max_integer([6, 5, 6], [5])

if __name__ == '__main__':
    unittest.main()
