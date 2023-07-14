#!/usr/bin/python3
"""A module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """init class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print class to stdout"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )
