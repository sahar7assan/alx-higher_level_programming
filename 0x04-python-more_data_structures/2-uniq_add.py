#!/usr/bin/python3
def uniq_add(my_list=[]):
    """function add all unique elements

    Args:
        my_list:list of element

    Returns:
        sum of elements
    """
    result = 0
    seen_elements = set()

    for element in my_list:
        if element not in seen_elements:
            result += element
            seen_elements.add(element)

    return result
