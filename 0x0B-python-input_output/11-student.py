#!/usr/bin/python3
"""Module that defines student class"""


class Student:
    """Definiton of student class"""
    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns json obj rep"""
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attrs of student"""
        for key, value in json.items():
            setattr(self, key, value)
