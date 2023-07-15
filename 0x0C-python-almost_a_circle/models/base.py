#!/usr/bin/python3
"""File containing module base class"""
import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """Create a new class instantiation
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from json file"""
        filename = f"{cls.__name__}.json"
        with open(filename, 'r') as f:
            try:
                list_file = []
                read_f = Base.from_json_string(f.read())
                for obj in read_f:
                    list_file.append(cls.create(**obj))
                return list_file
            except FileNotFoundError:
                return []
            except OSError:
                return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write to a csv file"""
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(
                        f,
                        fieldnames=fields
                        )
                writer.writeheader()
                for elem in list_objs:
                    writer.writerow(elem.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """read from a csv file"""
        pass
