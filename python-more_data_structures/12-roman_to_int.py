#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return (0)
    counter = 0
    list_roman = list(roman_string)
    list_roman.append("O")
    for c in range(len(list_roman)):
        if list_roman[0] == "I":
            if list_roman[c] == "I":
                counter = counter + 1
            elif list_roman[c] == "V":
                counter = 4
            elif list_roman[c] == "X":
                counter = 9
        elif list_roman[0] == "V":
            if list_roman[c] == "V":
                counter = counter + 5
            elif list_roman[c] == "I":
                counter = counter + 1
        elif list_roman[0] == "X":
            if list_roman[c] == "L":
                counter = counter + 30
            if list_roman[c] == "C":
                counter = counter + 80
            elif list_roman[c] == "X":
                counter = counter + 10
            elif list_roman[c] == "V":
                counter = counter + 5
            elif list_roman[c] == "I" and list_roman[-2] == "V":
                counter = counter + 4
                break
            elif list_roman[c] == "I" and list_roman[-2] == "X":
                counter = counter + 9
                break
            elif list_roman[c] == "I":
                counter = counter + 1
        elif list_roman[0] == "L":
            if list_roman[c] == "L":
                counter = counter + 50
            elif list_roman[c] == "X":
                counter = counter + 10
            elif list_roman[c] == "V":
                counter = counter + 5
            elif list_roman[c] == "I" and list_roman[-2] == "V":
                counter = counter + 4
                break
            elif list_roman[c] == "I" and list_roman[-2] == "X":
                counter = counter + 9
                break
            elif list_roman[c] == "I":
                counter = counter + 1
        elif list_roman[0] == "C":
            if list_roman[c] == "C" and list_roman[c + 1] == "M":
                counter = counter + 900
            elif list_roman[c] == "C" and list_roman[c + 1] == "D":
                counter = counter + 400
            elif list_roman[c] == "C" and list_roman[c-1] not in ("X", "D"):
                counter = counter + 100
            elif list_roman[c] == "L" and (
                    list_roman[c - 1] == "C" or
                    list_roman[c - 1] == "D"
            ):
                counter = counter + 50
            elif list_roman[c] == "X" and list_roman[c + 1] == "L":
                counter = counter + 40
            elif list_roman[c] == "X" and list_roman[c + 1] == "C":
                counter = counter + 90
            elif list_roman[c] == "X":
                counter = counter + 10
            elif list_roman[c] == "V":
                counter = counter + 5
            elif list_roman[c] == "I" and list_roman[-2] == "V":
                counter = counter + 4
                break
            elif list_roman[c] == "I" and list_roman[-2] == "X":
                counter = counter + 9
                break
            elif list_roman[c] == "I":
                counter = counter + 1
        elif list_roman[0] == "D":
            if list_roman[c] == "D" and list_roman[c - 1] != "C":
                counter = counter + 500
            elif list_roman[c] == "C" and list_roman[c + 1] == "D":
                counter = counter + 400
            elif list_roman[c] == "C" and list_roman[c - 1] != "X":
                counter = counter + 100
            elif list_roman[c] == "L" and list_roman[c - 1] == "C":
                counter = counter + 50
            elif list_roman[c] == "X" and list_roman[c + 1] == "L":
                counter = counter + 40
            elif list_roman[c] == "X" and list_roman[c + 1] == "C":
                counter = counter + 90
            elif list_roman[c] == "X":
                counter = counter + 10
            elif list_roman[c] == "V":
                counter = counter + 5
            elif list_roman[c] == "I" and list_roman[-2] == "V":
                counter = counter + 4
                break
            elif list_roman[c] == "I" and list_roman[-2] == "X":
                counter = counter + 9
                break
            elif list_roman[c] == "I":
                counter = counter + 1
        elif list_roman[0] == "M":
            if list_roman[c] == "M" and list_roman[c - 1] != "C":
                counter = counter + 1000
            elif list_roman[c] == "C" and list_roman[c + 1] == "M":
                counter = counter + 900
            elif list_roman[c] == "D" and list_roman[c - 1] != "C":
                counter = counter + 500
            elif list_roman[c] == "C" and list_roman[c + 1] == "D":
                counter = counter + 400
            elif list_roman[c] == "C" and list_roman[c - 1] != "X":
                counter = counter + 100
            elif list_roman[c] == "L" and list_roman[c - 1] == "C":
                counter = counter + 50
            elif list_roman[c] == "X" and list_roman[c + 1] == "L":
                counter = counter + 40
            elif list_roman[c] == "X" and list_roman[c + 1] == "C":
                counter = counter + 90
            elif list_roman[c] == "X":
                counter = counter + 10
            elif list_roman[c] == "V":
                counter = counter + 5
            elif list_roman[c] == "I" and list_roman[-2] == "V":
                counter = counter + 4
                break
            elif list_roman[c] == "I" and list_roman[-2] == "X":
                counter = counter + 9
                break
            elif list_roman[c] == "I":
                counter = counter + 1

    return (counter)
