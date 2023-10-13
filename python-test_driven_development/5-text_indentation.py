#!/usr/bin/python3
""" print square"""


def text_indentation(text):
    """prints a text with 2 new lines char: [.,?:]"""
    i = 0
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    else:
        try:
            while text[i]:
                print(text[i], end="")
                i += 1
                if text[i] in ['.', '?', ':']:
                    print(text[i], end="\n"*2)
                    i += 1
                    while text[i] == " ":
                        i += 1
        except:
            pass
