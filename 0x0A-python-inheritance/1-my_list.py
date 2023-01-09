#!/usr/bin/python3
"""
Module 1-my_list
Defines MyList subclass of list,
and private method
"""


class MyList(list):
    """
    Inherites from list class
    Functions:
      print_sorted
    """
    def print_sorted(self):
        """printed sorted list in ascending order"""
        print(sorted(self))
