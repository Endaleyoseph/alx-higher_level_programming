#!/usr/bin/python3
"""
Module 0-add_integer
Defines add_integer funtion
takes two numbers and add them
"""


def add_integer(a, b=98):
    """
    adds two integers and returns the the sum or raise TypeError
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
