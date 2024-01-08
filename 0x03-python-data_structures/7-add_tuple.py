#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Function add tuples

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        new tuple
    """
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
