#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    user = list(a_dictionary.keys())[0]
    max_n = a_dictionary[user]
    for key, val in a_dictionary.items():
        if val > max_n:
            big = val
            user = key
    return (user)
