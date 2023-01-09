#!/usr/bin/python3
"""
Module 2-is_same_class
Defines is_same_class
checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Returns true if it is, or False otherwise
    """
    return type(obj) == a_class
