#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """
    this class inherits from base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method"""
        Base.__init__(self, id)
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif self.__width <= 0:
            raise ValueError("width must be > 0")
        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif self.__height <= 0:
            raise ValueError("height must be > 0")
        self.__x = x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif self.__x < 0:
            raise ValueError("x must be >= 0")
        self.__y = y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif self.__y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """retrieving width"""
        return self.__width

    @width.setter
    def width(self, value):
        """managing width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieving Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """managing the Height"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """setting position_x"""
        return self.__x

    @x.setter
    def x(self, value):
        """managing position_x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """retrieving position_y"""
        return self.__y

    @y.setter
    def y(self, value):
        """managing position y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
