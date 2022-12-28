#!/usr/bin/python3
"""
Module 5-text_indentation
Defines text_indentation
prints a text in new line when ":","?", "."
"""


def text_indentation(text):
    """
    print a text in new line after ., :, ?
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for c in ".?:":
        text = text.replace(c, c + "\n\n")
    lines = [line.strip(" ") for line in text.split("\n")]
    final = "\n".join(lines)
    print(final, end="")
