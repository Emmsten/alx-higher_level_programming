#!/usr/bin/python3
"""Module MyList"""


class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        """Prints sorted lists"""
        print(sorted(self.copy()))
