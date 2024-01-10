#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """function that replaces all occurrences of an element

    Args:
        my_list: list of elements
        search: element search for
        replace: element replaced

    Returns:
         new list
    """
    new_list = [x if x != search else replace for x in my_list]
    return new_list
