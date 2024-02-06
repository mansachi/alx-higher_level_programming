#!/usr/bin/python3
"""This defines an inherited class-checking function."""


def inherits_from(obj, a_class):
"""This will check if an object is an inherited instance of a class.

Args:
obj (any): The is the object to be checked.
a_class (type): The class to match the type of obj to be checked.
Returns:
If obj is an inherited instance of a_class - True.
Otherwise - False.
"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

# end of code
