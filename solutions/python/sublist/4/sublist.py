"""This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def _contains(big: Sequence[T], small: Sequence[T]) -> bool:
    """Returns True if big contains small as a contiguous sublist.

    Args:
        big (Sequence[T]): The sequence to search within.
        small (Sequence[T]): The sequence to search for.

    Returns:
        bool: True if small is a contiguous sublist of big, False otherwise.
    """
    len_big = len(big)
    len_small = len(small)
    if len_small == 0:
        return True
    if len_small > len_big:
        return False
    for start in range(len_big - len_small + 1):
        if all(big[start + offset] == small[offset] for offset in range(len_small)):
            return True
    return False


def sublist(list_one: Sequence[T], list_two: Sequence[T]) -> int:
    """Returns the relationship between two sequences.

    The relationship can be one of the following:
    - SUBLIST: list_one is a sublist of list_two
    - SUPERLIST: list_one is a superlist of list_two
    - EQUAL: list_one and list_two are equal
    - UNEQUAL: list_one and list_two are unequal

    Args:
        list_one (Sequence[T]): The first sequence to compare.
        list_two (Sequence[T]): The second sequence to compare.

    Returns:
        int: An integer representing the relationship between the two sequences.
    """
    if list_one == list_two:
        return EQUAL
    if not list_one:
        return SUBLIST
    if not list_two:
        return SUPERLIST
    if _contains(list_two, list_one):
        return SUBLIST
    if _contains(list_one, list_two):
        return SUPERLIST
    return UNEQUAL
