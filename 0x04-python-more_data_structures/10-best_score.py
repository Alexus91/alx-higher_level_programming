#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value."""
    if a_dictionary:
        max_k = max(a_dictionary, key=a_dictionary.get)
        return (max_k)
    else:
        return (None)
