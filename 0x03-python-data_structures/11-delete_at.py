#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Function remove list item

    Args:
        my_list:list of integers

    Returns:
        None
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    if my_list is None:
        return (None)

    del my_list[idx]
    return (my_list)
