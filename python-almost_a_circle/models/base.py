#!/usr/bin/python3
""" base file """


class Base:
    """
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """converting json object to string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return (json.dumps([]))
        else:
            return (json.dumps(list_dictionaries))
    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = "{}.json".format(cls.__name__)

        json_dict = []

        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                for obj in list_objs:
                    dictionary = cls.to_dictionary(obj)
                    json_dict.append(dictionary)
                    dict_to_string = cls.to_json_string(json_dict)
                f.write(dict_to_string)
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
