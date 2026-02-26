"""This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one: list, list_two: list) -> int:
    """Returns the relationship between two lists.

    The relationship can be one of the following:
    - SUBLIST: list_one is a sublist of list_two
    - SUPERLIST: list_one is a superlist of list_two
    - EQUAL: list_one and list_two are equal
    - UNEQUAL: list_one and list_two are unequal

    Args:
        list_one (list): The first list to compare.
        list_two (list): The second list to compare.

    Returns:
        int: An integer representing the relationship between the two lists.
    """
    len_one = len(list_one)
    len_two = len(list_two)
    if list_one == list_two:
        return EQUAL
    if not list_two:
        return SUPERLIST
    if not list_one:
        return SUBLIST
    if len_one <= len_two:
        for idx in range(len_two - len_one + 1):
            if list_two[idx : idx + len_one] == list_one:
                return SUBLIST
    if len_two <= len_one:
        for idx in range(len_one - len_two + 1):
            if list_one[idx : idx + len_two] == list_two:
                return SUPERLIST
    return UNEQUAL
