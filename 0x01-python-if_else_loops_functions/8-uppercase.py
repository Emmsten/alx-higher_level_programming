#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            offset = ord('A') - ord('a')
            uppercase_char = chr(ord(char) + offset)
            print(uppercase_char, end="")
        else:
            print(char, end="")
    print()
