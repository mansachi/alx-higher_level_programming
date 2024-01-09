#!/usr/bin/python3
# 5-no_c.py code

def no_c(my_string):
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return new_string # end of code
