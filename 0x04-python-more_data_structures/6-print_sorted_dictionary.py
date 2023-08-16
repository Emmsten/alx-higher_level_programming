#!/usr/bin/python3
def print_sorted_dictionary(custom_dictionary):
    [print("{}: {}".format(i, custom_dictionary[i])) for i in sorted(custom_dictionary)]
