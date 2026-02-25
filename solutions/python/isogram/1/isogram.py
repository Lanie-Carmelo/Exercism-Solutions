"""Module to determine if a word is an isogram.

An isogram is a word that has no repeating letters, consecutive or non-consecutive,
though hyphens and spaces can appear multiple times.
"""


def is_isogram(string: str) -> bool:
    """Returns True if the input string is an isogram, and False otherwise.

    Args:
        string (str): The input string to check for being an isogram.
    Returns:        bool: True if the input string is an isogram, and False otherwise.
    """
    clean_string = string.replace(" ", "").replace("-", "").lower()
    return len(set(clean_string)) == len(clean_string)
