#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("{:d}: {:s}".format(i, argv[i]))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
        while i < len(argv):
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
