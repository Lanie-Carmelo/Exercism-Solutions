"""A pangram is a sentence that contains every single letter of the alphabet at least
once.

For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant). This module contains
a single function, is_pangram, that takes a string and returns True if the string is a
pangram, and False otherwise.
"""

from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)


def is_pangram(sentence: str) -> bool:
    """Returns true if the input string is a pangram, and false otherwise.

    Args:
        sentence (str): The string to check for pangram status.
    Returns:
        bool: True if the input string is a pangram, and false otherwise.
    """
    return ALPHABET.issubset(sentence.lower())
