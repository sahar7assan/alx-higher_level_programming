#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """function differnce element between 2 sets

    Args:
        set_1: first set
        set_2: second set

    Returns:
        differnce element
    """
    diff_set = set_1.symmetric_difference(set_2)
    return diff_set
