#!/usr/bin/python3
""" import json """
import json


class Base:
    """
    first class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json return the dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ json save"""
        with open(cls.__name__+'.json', 'w+', encoding="utf-8") as file:
            dict = []
            if list_objs is not None and len(list_objs) != 0:
                for i in list_objs:
                    dict.append(cls.to_dictionary(i))
                file.write(cls.to_json_string(dict))
            else:
                file.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """return list"""
        if json_string is not None:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):

        dummy = cls(1, 1)
        dummy.x = 0
        dummy.y = 0
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        file = cls.__name__ + ".json"
        try:
            with open(file, 'r') as f:
                return [cls.create(**dictionary) for
                        dictionary in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []
