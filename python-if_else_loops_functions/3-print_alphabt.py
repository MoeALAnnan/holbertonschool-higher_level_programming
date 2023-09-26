#!/usr/bin/python3
for i in range(97, 123):
    if i == ord('e') or i == ord('q'):
        i += 1
    print(f"{chr(i)}".format(i), end="")
