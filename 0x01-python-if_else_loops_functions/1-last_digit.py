#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)

if number < 0:
    last = number % -10
else:
    last = number % 10

if last > 5:
    print("Last digit of {:d} is {:d}".format(number, last), end=" ")
    print("and is greater than 5")
elif last == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last))
else:
    print("Last digit of {:d} is {:d}".format(number, last), end=" ")
    print("and is less than 6 and not 0")
