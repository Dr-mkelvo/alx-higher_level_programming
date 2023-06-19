#!/usr/bin/python3
"""Defining a method (save_to_json_file)."""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        json.dump(my_obj, f)
