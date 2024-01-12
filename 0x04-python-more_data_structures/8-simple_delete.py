#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """function delete key

    Args:
        a_dictionary: dictionary
        key: key

    Returns:
        dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
        return (a_dictionary)
    else:
        return (a_dictionary)
