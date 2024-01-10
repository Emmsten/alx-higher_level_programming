#!/usr/bin/python3

def best_score(custom_dictionary):
    if custom_dictionary:
        return max(custom_dictionary, key=custom_dictionary.get)
    else:
        return None
