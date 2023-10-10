#!/usr/bin/python3
""" a class the defines a square """


class Square:
    """ a class that defines a square by size """
    def __init__(self, size=0):
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
