#!/usr/bin/python3
"""Defining a method(append_after)."""


def append_after(filename="", search_string="", new_string=""):
    """
    """
    text = ""
    with open(filename) as r:
        for i in r:
            text += i
            if search_string in i:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
