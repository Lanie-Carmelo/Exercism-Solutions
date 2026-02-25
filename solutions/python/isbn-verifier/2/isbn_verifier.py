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
    clean_isbn = isbn.replace("-", "").replace(" ", "")
    # Check if the cleaned ISBN has exactly 10 characters
    if len(clean_isbn) != 10:
        return False
    total_sum = 0
    for char_index, char in enumerate(clean_isbn):
        if char.isdigit():
            total_sum += int(char) * (10 - char_index)
        elif char == "X" and char_index == 9:
            total_sum += 10
        else:
            return False  # Invalid character or 'X' in the wrong position
    return total_sum % 11 == 0
