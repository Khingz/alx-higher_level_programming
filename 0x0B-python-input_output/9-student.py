#!/usr/bin/python3
"""Module that defines student class"""


class Student:
    """Definiton of student class"""
    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns json obj rep"""
        return self.__dict__
