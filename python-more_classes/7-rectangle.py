#!/usr/bin/python3
""" This will be an excercise
    to practice class and objects
"""


class Rectangle:
    """ Class that defines a Rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ this method returns the area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ this method returns the parameter """
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """ this is special method """
        str1 = ""
        if self.__height == 0 or self.__width == 0:
            return str1
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    str1 = str1 + str(self.print_symbol)
                if i != (self.__height - 1):
                    str1 = str1 + "\n"
            return (str1)

    def __repr__(self):
        """ this is another special method """
        return "{}({}, {})".format(type(self).__name__,
                                   self.__width, self.__height)

    def __del__(self):
        """ destructor method """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
