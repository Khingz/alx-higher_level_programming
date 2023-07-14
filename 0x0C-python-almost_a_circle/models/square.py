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
