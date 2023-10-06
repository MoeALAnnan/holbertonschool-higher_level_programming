#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if (x == 0) or not my_list:
        print("")
        return (0)
    try:
        s = ""
        for i in range(0, x):
            s1 = str(my_list[i])
            s = s+s1
        c = int(s)
        print(c)
        return (x)
    except IndexError:
        pass
    sc = ""
    for z in range(0, my_list[-1]):
        s2 = str(my_list[z])
        sc = sc+s2
    d = int(sc)
    print(d)
    return (my_list[-1])
