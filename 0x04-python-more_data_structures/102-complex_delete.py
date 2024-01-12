#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """function delete  keys with a specific value in a dictionary

    Args:
        a_dictionary: dictionary
        value: value

    Returns:
        new dictionary
    """
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
