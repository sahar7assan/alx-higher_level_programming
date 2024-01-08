#!/usr/bin/python3
def multiple_returns(sentence):
    """Function return length and first char

    Args:
        sentence: string

    Returns:
        tuple
    """
    length = len(sentence)
    if length > 0:
        first = sentence[0]

    else:
        first = None
    return (length, first)
