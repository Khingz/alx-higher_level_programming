#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square.
    Args:
        size (int): The size of the new square.

    """
    def __init__(self, size=0):
        """initialize propertirs"""
        self.size = size

    @property
    def size(self):
        """get the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """updates the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current area of square"""
        return self.__size * self.__size
