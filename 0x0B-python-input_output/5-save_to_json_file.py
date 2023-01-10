#!/usr/bin/python3
"""
Module 5-save_to_json_file
Defines save_to_json_file
writes object to text file
"""


import json


def save_to_json_file(my_obj, filename):
    """from object to JSON file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
