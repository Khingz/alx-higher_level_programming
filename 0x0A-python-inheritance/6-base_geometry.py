#!/usr/bin/python3
"""Contains class definition for Geometry"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """defines the area"""
        raise Exception("area() is not implemented")
