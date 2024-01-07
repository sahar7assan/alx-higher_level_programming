#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """function replace element

    Args:
        my_list:list element
        idx:element index
        element: element to replace

    Returns:
        new list
    """
    length = len(my_list)
    if idx < 0:
        return my_list

    if idx < length:
        my_list[idx] = element
        return my_list
    else:
        return my_list
