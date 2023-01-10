#!/usr/bin/python3
"""
Module 8-class_to_json
Defines class_to_json
from to class to json
"""


def class_to_json(obj):
    """Returns dictionary description"""
    return obj.__dict__
