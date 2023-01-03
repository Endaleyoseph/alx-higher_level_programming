#!/usr/bin/python3
"""
Module 101-locked_class
Defines LockedClass with no 
class or object attribute
"""


class LockedClass:
    """
    controls dynamic creation of instance attribute
    """
    __slots__ = "first_name"
