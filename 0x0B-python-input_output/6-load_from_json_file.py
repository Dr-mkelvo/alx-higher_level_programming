#!/usr/bin/python3
"""Defining a method (load_from_json_file)."""
import json


def load_from_json_file(filename):
    with open(filename) as my_file:
        return json.load(my_file)
