#!/usr/bin/python3
"""
Module 1-write_file
Defines write_file
writes a string to text file
"""


def write_file(filename="", text=""):
    """Returns the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
