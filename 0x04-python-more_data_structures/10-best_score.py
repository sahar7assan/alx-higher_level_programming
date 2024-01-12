#!/usr/bin/python3
def best_score(a_dictionary):
    """function return key with the biggest integer value

    Args:
        a_dictionary: dictionary

    Returns:
        max value
    """
    if not a_dictionary:
        return None

    max_value = 0
    max_key = None

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key
