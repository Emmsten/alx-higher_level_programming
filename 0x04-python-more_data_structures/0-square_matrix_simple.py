#!/usr/bin/python3

def square_matrix_simple(custom_matrix=[]):
    result = []
    for custom_sublist in custom_matrix:
        squared_sublist = []
    for num in custom_sublist:
        squared_sublist.append(num ** 2)
        result.append(squared_sublist)    
return result
