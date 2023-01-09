#!/usr/bin/python3
"""
Module 100-my_int
Defines MyInt
Inherites from int
"""


class MyInt(int):
    """
    Class MyInt that has opposite operators
    Funtions
       __eq__
       __neq__
    Args:
     value (int): integer
    """
    def __init__(self, value):
        """
        initilizes Myint
        """
        self.value = value

    def __eq__(self, other):
        """
        Args:
         other (int): integer
        returns True if self is not equal
        """
        return self.value != other

    def __ne__(self, other):
        """
        Args:
         other (int): integer
        return True if self is equal
        """
        return self.value == other
