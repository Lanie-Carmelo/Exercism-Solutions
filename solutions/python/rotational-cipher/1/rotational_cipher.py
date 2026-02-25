"""This module implements a rotational cipher, also sometimes called a Caesar cipher.

It is a simple letter substitution cipher that replaces a letter with the letter that is
a fixed number of positions down the alphabet. For example, with a key of 13, 'A' would
be replaced by 'N', 'B' would become 'O', and so on. The same transformation is applied
to lowercase letters, while non-alphabetic characters are left unchanged.
"""


def rotate(text: str, key: int) -> str:
    """Applies a rotational cipher to the given text using the specified key.

    Args:
        text (str): The input string to be transformed.
        key (int): The number of positions to rotate each letter.
    Returns:
        str: The transformed string after applying the rotational cipher.
    """
    chars = []
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            rotated_char = chr((ord(char) - base + key) % 26 + base)
            chars.append(rotated_char)
        else:
            chars.append(char)
    return "".join(chars)
