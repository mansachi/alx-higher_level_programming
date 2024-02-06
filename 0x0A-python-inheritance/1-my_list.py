#!/usr/bin/python3
"""
This will Defines MyList that inherits from list
"""


class MyList(list):
"""
This is a class inherited from list.
Attributes:
Methods:
print_sorted - this will print the list in ascending order
"""
    def print_sorted(self):
"""
this will print a list in ascending order.
"""
    print(sorted(self))

# end of code
