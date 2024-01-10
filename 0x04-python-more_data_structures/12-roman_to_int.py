#!/usr/bin/python3

def roman_to_int(custom_roman_string):
    if not custom_roman_string or not isinstance(custom_roman_string, str):
        return 0    total = 0    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(custom_roman_string) - 1, -1, -1):
        intVal = digits[custom_roman_string[i]]
        total += intVal if total < intVal * 5 else -intVal
    return total
