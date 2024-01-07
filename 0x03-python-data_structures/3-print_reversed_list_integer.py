#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function reverse list element

    Args:
        my_list:list of integers

    Returns:
        None
    """
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
