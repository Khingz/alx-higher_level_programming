#!/usr/bin/python3
"""File containing module base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert dict to a json strin"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves dict to a file"""
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as f:
            new_list = []
            if list_objs is None:
                f.write("[]")
            elif isinstance(list_objs, list):
                for elem in list_objs:
                    if isinstance(elem, cls):
                        di = elem.to_dictionary()
                        new_list.append(di)
                f.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """converts json object to dict"""
        if json_string is None:
            return []
        return json.loads(json_string)
