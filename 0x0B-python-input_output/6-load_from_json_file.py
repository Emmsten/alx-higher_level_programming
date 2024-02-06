#!/usr/bin/python3
"""
Contains the load_from_json_file function
"""

def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, 'r') as f:
        return f.read()
