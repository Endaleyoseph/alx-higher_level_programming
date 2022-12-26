#!/usr/bin/python3
"""
Module 2-say_my_name
Defines sya_my_name
prints the first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    takes first and last name and prints it
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
