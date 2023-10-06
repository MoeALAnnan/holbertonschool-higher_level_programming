#!/usr/bin/python3
def raise_exception():
    str1 = ""
    num = 5
    try:
        num = str1 + num
    except TypeError:
        raise
