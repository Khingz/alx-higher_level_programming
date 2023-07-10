#!/usr/bin/python3
"""Contains class definition for Geometry"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """defines the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value input"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value < 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """Class rectangle, child class og baseGeometry"""
    def __init__(self, width, height):
        """init function"""
        self.integer_validator("", width)
        self.__width = width
        self.integer_validator("", height)
        self.__height = height
