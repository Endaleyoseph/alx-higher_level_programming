#!/usr/bin/python3
"""
Module 7-add_item

main
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    list_t = load_from_json_file(filename)
except FileNotFoundError:
    list_t = []

save_to_json_file(list_t + argv[1:], filename)
