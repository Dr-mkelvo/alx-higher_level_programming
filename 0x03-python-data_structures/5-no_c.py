#!/usr/bin/python3
def no_c(my_string):
    blank_string = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            blank_string += i
    return blank_string 
