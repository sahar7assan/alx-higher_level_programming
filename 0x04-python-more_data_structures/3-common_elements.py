#!/usr/bin/python3
def common_elements(set_1, set_2):
    """function common elements between 2 sets

    Args:
        set_1: first set
        set_2: second set

    Returns:
        common element
    """
    common_set = set_1.intersection(set_2)
    return common_set
