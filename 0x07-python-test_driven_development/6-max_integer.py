#!/usr/bin/python3
""" A function that gets the max number in a list"""


def max_integer(list=[]):
    """
    """
    if len(list) == 0:
        return None
    result = list[0]
    num = 1
    while num < len(list):
        if list[num] > result:
            result = list[num]
        num += 1
    return result
