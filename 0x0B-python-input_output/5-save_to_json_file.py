#!/usr/bin/python3
"""
Contains the save_to_json_file function
"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w') as f:
        f.write(str(my_obj))
