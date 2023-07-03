#!/usr/bin/python3
"""Defines a class rectngle"""


class Rectangle:
    """Represents a class"""
    def __init__(self, width=0, height=0):
        """
        init class instance

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @width.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """compute the area"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__width * self.__height

    def perimeter(self):
        """compute the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """prints matrix"""
        mat = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            mat += ("#" * self.__width)
            mat += '\n' if i != (self.__height - 1) else ""
        return mat
