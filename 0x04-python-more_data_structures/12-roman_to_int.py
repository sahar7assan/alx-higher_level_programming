#!/usr/bin/python3
def roman_to_int(roman_string):
    """function  converts a Roman numeral to an integer.

    Args:
       a_dictionary: roman_string

    Returns:
        value of roman number
    """

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    nu = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(roman_string)):
        if (
            i < len(roman_string) - 1
            and nu[roman_string[i]] < nu[roman_string[i + 1]]
        ):

            result -= nu[roman_string[i]]
        else:
            result += nu[roman_string[i]]

    if 1 <= result <= 3999:
        return result
    else:
        return 0
