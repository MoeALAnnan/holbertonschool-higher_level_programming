#!/usr/bin/python3
for i in range(99):
    print(f"{i:02}, ".format(i), end="")
    if i == 98:
        print(f"{i+1}".format(i))
