#!/usr/bin/python3
def isupper(str):
    for i in str:
        new_line = "\n"
        if ord(i) in range(97, 123):
            i = chr(ord(i) - 32)
        print(f"{i}".format(i), end="")
    print(f"{new_line}".format(new_line))
