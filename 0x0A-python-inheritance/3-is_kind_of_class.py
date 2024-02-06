#!/usr/bin/python3
"""This will define a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
"""This will check if an object is an instance or inherited instance of a class.

Args:
obj (any): The object to be checked.
a_class (type): This class will match the type of obj to be checked.
Returns:
If obj is an instance or inherited instance of a_class - True.
Otherwise - False.
"""
    if isinstance(obj, a_class):
        return True
    return False

# end of code
