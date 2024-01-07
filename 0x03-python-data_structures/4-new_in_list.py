#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """function replace element without modify

    Args:
        my_list:list element
        idx:element index
        element: element to replace

    Returns:
        new list
    """
    length = len(my_list)
    list_copy = my_list.copy()
    if idx < 0:
        return list_copy

    if idx < length:
        list_copy[idx] = element
        return list_copy
    else:
        return list_copy
