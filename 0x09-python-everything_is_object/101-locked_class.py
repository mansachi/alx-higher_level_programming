#!/usr/bin/python3
"""This will define a locked class."""

class LockedClass:
    """
    This will prevent the user from instantiating new LockedClass attributes
    for anything else except for attributes called 'first_name'.
    """

    __slots__ = ("first_name")
# end of code
