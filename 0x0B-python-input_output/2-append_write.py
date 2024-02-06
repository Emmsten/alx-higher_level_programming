#!/usr/bin/python3
"""
Contains the append_write function
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the number of characters added"""
    try:
        with open(filename, "a", encoding="utf-8") as f:
            return f.write(text)
    except FileNotFoundError:
        with open(filename, "w", encoding="utf-8") as f:
            return f.write(text)
