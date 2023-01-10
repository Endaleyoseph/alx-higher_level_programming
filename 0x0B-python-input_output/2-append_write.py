#!/usr/bin/python3
"""
Module 1-write_file
Defines append_write
appends a string at the end of text file
"""


def append_write(filename="", text=""):
    """Returns the number of characters written"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
