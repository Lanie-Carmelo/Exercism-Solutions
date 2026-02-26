"""Translate text to Pig Latin.

This module provides a function `translate` that takes a string of text
and converts it to Pig Latin, a made-up children's language.
"""

VOWELS = "aeiou"
QU = "qu"


def split_index(word: str) -> int:
    """Return the index where the vowel sound begins.

    Args:
        word (str): A single English word.

    Returns:
        int: The index where the vowel sound begins for rotation rules.
        Returns 0 if no vowel sound is found.
    """
    word_lower = word.lower()
    index = 0

    while index < len(word_lower):
        # Treat "qu" as a consonant sound
        if word_lower[index : index + len(QU)] == QU:
            index += len(QU)
            continue

        # "y" acts as a vowel if not at the start
        if word_lower[index] == "y" and index > 0:
            return index

        # Regular vowels
        if word_lower[index] in VOWELS:
            return index

        index += 1

    return 0


def translate_word(word: str) -> str:
    """Translate a single word to Pig Latin.

    Args:
        word (str): A string representing a single word.

    Returns:
        str: A string representing the translated word in Pig Latin.
    """
    if not word:
        return word
    word_lower = word.lower()
    if (
        word_lower[0] in VOWELS
        or word_lower.startswith("xr")
        or word_lower.startswith("yt")
    ):
        return word + "ay"
    idx = split_index(word)
    return word[idx:] + word[:idx] + "ay"


def translate(text: str) -> str:
    """Translate a string of text to Pig Latin.

    Args:
        text (str): A string of text to be translated.

    Returns:
        str: A string of text translated to Pig Latin.
    """
    return " ".join(translate_word(word) for word in text.split())
