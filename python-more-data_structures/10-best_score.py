#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        if a_dictionary != {}:
            new_dictionary = dict(sorted(a_dictionary.items(),
                                         key=lambda x: x[1]))
            return (new_dictionary.popitem()[0])
        else:
            return
