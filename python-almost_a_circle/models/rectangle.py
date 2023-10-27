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

    def area(self):
        """returning area"""
        return (self.__width * self.__height)

    def display(self):
        """displaying the rectangle"""
        for m in range(self.__y):
            print("")
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """magic method"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """updating arguments"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "height":
                        self.__height = value
                    elif key == "width":
                        self.__width = value
                    elif key == "x":
                        self.__x = value
                    elif key == "y":
                        self.__y = value
                    elif key == "id":
                        self.id = value

    def to_dictionary(self):
        """returning dictionary representation"""
        dic1 = {"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width}
        return (dic1)
