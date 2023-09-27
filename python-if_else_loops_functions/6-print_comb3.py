#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i + j == 17:
            continue
        print(f"{i}{j}, ".format(i, j), end="")
print(f"{i-1}{j}".format(i, j))