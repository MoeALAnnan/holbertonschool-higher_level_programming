#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    a = 10
    b = 5

    print(f"{a} + {b} = {add(a, b)}\n"
          f"{a} - {b} = {sub(a, b)}\n"
          f"{a} * {b} = {mul(a, b)}\n"
          f"{a} / {b} = {div(a, b)}"
          .format(a, b, add(a, b), sub(a, b), mul(a, b), div(a, b)))
