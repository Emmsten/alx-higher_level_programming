#!/usr/bin/python3

def search_replace(custom_list, search, replace):
    return list(map(lambda n: replace if n == search else n, custom_list))
