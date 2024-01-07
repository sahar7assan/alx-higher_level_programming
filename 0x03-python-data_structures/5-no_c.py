#!/usr/bin/python3
def no_c(my_string):
    """function remove char from string

    Args:
        my_string: string

    Returns:
        new string
    """
    chars = ["c", "C"]
    modified_str = "".join(char for char in my_string if char not in chars)
    return modified_str
