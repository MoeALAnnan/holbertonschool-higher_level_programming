#!/usr/bin/python3
for i in range(97, 123):
    if i != ord('e') and i != ord('q'):
        print(f"{chr(i)}".format(i), end="")
