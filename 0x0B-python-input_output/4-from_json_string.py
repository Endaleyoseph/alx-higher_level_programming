#!/usr/bin/python3
"""
Module 4-from_json_string.py
Define from_json_string
JSON representation of object to python data
"""


import json


def from_json_string(my_str):
    """Returns to python data structure"""
    return json.loads(my_str)
