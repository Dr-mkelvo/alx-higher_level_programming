#!/usr/bin/python3
def no_c(my_string):
    empty_str = ""
    for element in my_string:
        if element != 'C' and element != 'c':
            empty_str += element
    return empty_str
