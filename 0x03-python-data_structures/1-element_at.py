#!/usr/bin/python3
def element_at(my_list, idx):
    """retrieves an elemen

    Args:
        my_list:list element
        idx:element index

    Returns:
        element in index idx
    """
    length = len(my_list)
    if idx < 0:
        return None
    if idx < length:
        return my_list[idx]
    else:
        return None
