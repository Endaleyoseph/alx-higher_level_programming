#!/usr/bin/python3
"""
Module 0-read_file
Defines read_file
reads a text file
"""


def read_file(filename=""):
    """Prints text in file to stdout"""
    with open(filename) as f:
        for line in f:
            print(line, end='')
