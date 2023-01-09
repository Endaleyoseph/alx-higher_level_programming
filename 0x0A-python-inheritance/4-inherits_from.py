#!/usr/bin/python3
"""
Modlue 4-inherits_from
Define inherits_from
checks if the object is an instance of class,
"""


def inherits_from(obj, a_class):
    """
    Returns True if it is, or False other wise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
