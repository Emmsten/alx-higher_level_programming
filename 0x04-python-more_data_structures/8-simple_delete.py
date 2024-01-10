#!/usr/bin/python3

def simple_delete(custom_dictionary, custom_key=""):
    if custom_key in custom_dictionary:
        del custom_dictionary[custom_key]
    return custom_dictionary
