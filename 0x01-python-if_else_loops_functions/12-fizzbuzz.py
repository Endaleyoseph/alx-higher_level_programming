#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz ', end='')
        elif i % 3 == 0:
            print('FIZZ ', end='')
        elif i % 5 == 0:
            print('BUZZ ', end='')
        else:
            print('{} '.format(i), end='')
