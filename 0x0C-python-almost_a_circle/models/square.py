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
        """setter for soze attribute"""
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

    def update(self, *args, **kwargs):
        """update the values of the class"""
        if args and len(args) != 0:
            arg_count = 0
            for arg in args:
                if arg_count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif arg_count == 1:
                    self.size = arg
                elif arg_count == 2:
                    self.x = arg
                elif arg_count == 3:
                    self.y = arg
                arg_count += 1

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """returns dict rep"""
        """return self.__dict__"""
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
        }
