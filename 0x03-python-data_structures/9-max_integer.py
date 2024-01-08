#!/usr/bin/python3
def max_integer(my_list=[]):
    """Function finds the biggest integer of a list

    Args:
        my_list:list of integers

    Returns:
        max element
    """
    length = len(my_list)
    if length == 0:
        return None
    max_num = my_list[0]
    for n in my_list:
        if n > max_num:
            max_num = n
    return max_num
