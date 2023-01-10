#!/usr/bin/python3
"""
Module 6-load_from_json_file
Defines load_from_json_file
writes text file to object
"""


import json


def load_from_json_file(filename):
    """from JSON file to object"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
