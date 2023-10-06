#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            my_list[i] += 0
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError):
            continue
    print("")
    return (count)
