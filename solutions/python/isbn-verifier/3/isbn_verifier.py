"""Module for validating ISBN-10 numbers.

A valid ISBN-10 number is a 10-character string that consists of digits (0-9) and may
end with an 'X' (which represents the value 10). The validation process involves
calculating a weighted sum of the digits and checking if it is divisible by 11. The
weights for the digits are as follows: the first digit is multiplied by 10, the second
digit by 9, the third digit by 8, and so on, until the tenth digit is multiplied by 1.
If the total sum is divisible by 11, the ISBN-10 number is considered valid. The
function should return True if the ISBN-10 number is valid and False otherwise.
"""


def is_valid(isbn: str) -> bool:
    """Check if the given ISBN-10 number is valid.

    Args:
        isbn (str): The ISBN-10 number to validate.
    Returns:
        bool: True if the ISBN-10 number is valid, False otherwise.
    """
    # Remove any hyphens or spaces from the input
    clean = "".join(char for char in isbn if char not in "- ")

    if len(clean) != 10:
        return False

    total = 0

    for char, weight in zip(clean, range(10, 0, -1)):
        if char == "X":
            if weight != 1:
                return False
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False
        total += value * weight
    return total % 11 == 0
