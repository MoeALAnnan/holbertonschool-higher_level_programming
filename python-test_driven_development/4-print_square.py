#!/usr/bin/python3
""" print square"""


def print_square(size):
    """square with the character #"""
    if isinstance(size, int) is False:
        raise ValueError('size must be an integer')
    if isinstance(size, int) is True and size < 0:
        raise TypeError('size must be >= 0')
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print('')
