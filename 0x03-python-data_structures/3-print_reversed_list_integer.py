#!/usr/bin/python3
def print_reversed_list_integer(custom_list=[]):
    if custom_list is None:
        return
    for num in reversed(custom_list):
        print("{:d}".format(num))
