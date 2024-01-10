#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """function prints a dictionary by ordered keys

    Args:
        a_dictionary: dictionary

    Returns:
        print sorted dictionary
    """
    sorted_items = sorted(a_dictionary.items())
    sorted_dict = dict(sorted_items)
    for key in sorted_dict:
        print("{}: {}".format(key, sorted_dict[key]))
