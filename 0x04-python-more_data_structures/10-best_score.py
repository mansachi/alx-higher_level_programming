#!/usr/bin/python3
# code for 10-best_score.py

def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))
# end of code
