#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (TypeError, ValueError, ZeroDivisionError, IndexError) as inst:
        sys.stderr.write("Exception: {}\n".format(inst))
        return None
