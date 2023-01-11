#!/usr/bin/python3
"""
module 101-stats
Input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C).
prints those statistics since the beginning
"""

import sys


def print_status_code(size, status_code):
    """prints number and status code"""
    print("File size: {:d}".format(size))
    for key, value in sorted(status_code.items()):
        if value:
            print("{:s}: {:d}".format(key, value))


def read_stdin_compute():
    size = 0
    lines = 0
    status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
                   "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            list_t = list(map(str, line.strip().split(" ")))
            size += int(list_t[-1])
            if list_t[-2] in status_code.keys():
                status_code[list_t[-2]] += 1
            lines += 1
            if lines % 10 == 0:
                print_status_code(size, status_code)
    except KeyboardInterrupt:
        print_status_code(size, status_code)
        raise

    print_status_code(size, status_code)


read_stdin_compute()
