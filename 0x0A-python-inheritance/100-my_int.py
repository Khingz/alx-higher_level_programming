#!/usr/bin/python3
"""A class that extends from int"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, value):
        """defines equal"""
        if isinstance(value, int):
            return self.real != value

    def __ne__(self, value):
        """defines not equal"""
        if isinstance(value, int):
            return self.real == value
