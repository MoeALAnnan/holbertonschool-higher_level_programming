#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k in a_dictionary.keys():
        if k == key:
            del a_dictionary[key]
            break
    return (a_dictionary)
