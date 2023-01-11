#!/usr/bin/python3
"""
Module 100-append_after
Define append_after
searchs for a string and adds a text
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line in a text file"""
    content = []
    with open(filename, mode="r") as f:
        for line in f:
            content.append(line)
        f.seek(0)

    for i in range(len(content)):
        if search_string in content[i]:
            if i == len(content) - 1:
                content.append(new_string)
            else:
                content.insert(i + 1, new_string)

    with open(filename, mode="w") as f:
        for line in content:
            f.write(line)
