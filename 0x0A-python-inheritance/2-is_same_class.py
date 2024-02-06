#!/usr/bin/python3
"""This will defines a class-checking function only."""


def is_same_class(obj, a_class):
"""Check if an object is exactly an instance of a given class.

Args:
obj (any): This is the object to be checked.
a_class (type): The class to match the type of obj to.
Returns:
If obj is exactly an instance of a_class - True.
Otherwise - False.
"""
    if type(obj) == a_class:
        return True
    return False

# end of code
