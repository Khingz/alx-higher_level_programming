#!/usr/bin/python3
"""Contains class definition for Geometry"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """defines the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value input"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
