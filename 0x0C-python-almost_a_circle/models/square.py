#!/usr/bin/python3
"""A module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """print class to stdout"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )

    def update(self, *args, **kargs):
        """update the values of the class"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for elem in kargs.keys():
                if hasattr(self, elem):
                    setattr(self, elem, kargs[elem])

    def to_dictionary(self):
        """returns dict rep"""
        """return self.__dict__"""
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
        }
