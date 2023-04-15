#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    i = 0

    for letter in str:
        if i != n:
            new_string += letter
        i += 1

    return new_string
