"""
An Armstrong number is an n-digit number that is equal to the sum of the nth powers of its digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
"""

def is_armstrong_number(number: int) -> bool:
    """
    Check if the given number is an Armstrong number.

    Args:
        number (int): The number to check.
    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer.")
    # Convert the number to a string to easily access each digit.
    digits = str(number)
    # Get the number of digits (n).
    num_digits = len(digits)
    # Calculate the sum of the nth powers of the digits.
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    return armstrong_sum == number
