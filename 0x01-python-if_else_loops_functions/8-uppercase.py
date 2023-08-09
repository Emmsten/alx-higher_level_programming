#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            offset = ord('A') - ord('a')
            uppercase_char = chr(ord(char) + offset)
            result += "{}".format(uppercase_char)
        else:
            result += "{}".format(char)
    print(result)
