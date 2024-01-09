#!/usr/bin/python3
# 2-replace_in_list.py code

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list # end of code
