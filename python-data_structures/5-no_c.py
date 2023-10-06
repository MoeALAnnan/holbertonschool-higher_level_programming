#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    new_list = [x for x in my_list if x != 'c' and x != 'C']
    new_string = ''.join(new_list)
    return new_string
