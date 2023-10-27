#!/usr/bin/python3
"""class Square"""
from models.rectangle import Rectangle


"""class Square"""


class Square(Rectangle):
    """class Square that imports from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """new init"""
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """ overloading of str method """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """updating the values of args and kwargs"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                    self.height = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self.size = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """returning dictionary representation of square"""
        dic1 = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return (dic1)
