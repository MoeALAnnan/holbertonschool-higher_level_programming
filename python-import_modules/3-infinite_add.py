#!/usr/bin/python3
import sys
argv = sys.argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0")
    elif len(argv) == 2:
        print(f"{argv[1]}")
    elif len(argv) >= 2:
        x = len(argv) - 1
        y = 0
        for i in range(x):
            y = y + int(argv[i + 1])
        print(f"{y}")
