#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            offset = ord('A') - ord('a')
            uppercase_char = chr(ord(char) + offset)
            print("{}".format(uppercase_char), end="")
        else:
            print("{}".format(char), end="")
    print()
