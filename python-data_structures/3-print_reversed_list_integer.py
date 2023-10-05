#!/usr/bin/python3

# def print_reversed_list_integer(my_list=[]):
# for i in range (len(my_list)):
# print(f"{my_list[- i - 1]}".format(my_list[-i- 1]))
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        my_list.reverse()
        for x in my_list:
            print("{:d}".format(x))
