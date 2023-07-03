#!/usr/bin/python3
"""Defines a class rectngle"""


class Rectangle:
    """Represents a class"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """
        init class instance

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
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

    def __repr__(self):
        """prints matrix"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """del an instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
