#!/usr/bin/python

"""
contains the lookup function
"""

def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
