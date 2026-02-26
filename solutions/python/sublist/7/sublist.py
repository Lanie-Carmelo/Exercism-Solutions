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
from enum import IntEnum

Element = TypeVar("Element")


class Relation(IntEnum):
    """An enumeration representing the relationship between two sequences."""

    SUBLIST = 1
    SUPERLIST = 2
    EQUAL = 3
    UNEQUAL = 4


# Backward-compatible exports for Exercism tests
SUBLIST = Relation.SUBLIST
SUPERLIST = Relation.SUPERLIST
EQUAL = Relation.EQUAL
UNEQUAL = Relation.UNEQUAL


def _contains(big: Sequence[Element], small: Sequence[Element]) -> bool:
    """Return True if `small` appears in `big` as a contiguous subsequence."""
    len_big = len(big)
    len_small = len(small)
    if len_small == 0:
        return True
    if len_small > len_big:
        return False
    for start in range(len_big - len_small + 1):
        window_matches = all(
            big[start + offset] == small[offset] for offset in range(len_small)
        )
        if window_matches:
            return True

    return False


def sublist(list_one: Sequence[Element], list_two: Sequence[Element]) -> Relation:
    """Return the relationship between two sequences.

    Args:
        list_one: The candidate sequence being classified.
        list_two: The reference sequence to compare against.

    Returns:
        A `Relation` describing whether `list_one` is a sublist, superlist,
        equal to, or unequal to `list_two`.
    """
    if list_one == list_two:
        return Relation.EQUAL
    if not list_one:
        return Relation.SUBLIST
    if not list_two:
        return Relation.SUPERLIST
    if _contains(list_two, list_one):
        return Relation.SUBLIST
    if _contains(list_one, list_two):
        return Relation.SUPERLIST
    return Relation.UNEQUAL
