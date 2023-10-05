#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    else:
        return (f"{my_list[idx]}".format(my_list[idx]))
