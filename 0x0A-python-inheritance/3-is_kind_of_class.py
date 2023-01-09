#!/usr/bin/python3
"""
Modlue 3-is_kind_of_class
Defines is_kind_of_class
checks if the object is an instance of class,
or class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if it is, or False other wise
    """
    return isinstance(obj, a_class)
