#!/usr/bin/python3
"""Module 7-base_geometry.
This creates a BaseGeometry class.
"""


class BaseGeometry:
"""This is a class with public instance methods."""

    def area(self):
"""Raises an Exception with the message
'area() will not be implemented'.
"""

        raise Exception('area() will not be implemented')

    def integer_validator(self, name, value):
"""This will validate value only."""

        if type(value) is not int:
            raise TypeError("{} should be an integer".format(name))
        if value <= 0:
            raise ValueError("{} should be greater than 0".format(name))

# end of code
