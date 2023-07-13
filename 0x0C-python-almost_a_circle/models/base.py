#!/usr/bin/python3
"""File containing module base class"""


class Base:
    """Module base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
