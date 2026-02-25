"""Create numbered deli tickets with proper English ordinal formatting.

This module formats a sentence announcing a customer's position in line, converting
numbers from 1 to 999 into their correct ordinal form (e.g., 1st, 2nd, 3rd, 4th).
"""


def get_ordinal_suffix(value: int) -> str:
    """Determines the correct ordinal suffix for a given number.

    Args:
        value (int): The number to determine the ordinal suffix for.
    Returns:
        str: The ordinal suffix for the given number.
    """
    if value < 1 or value > 999:
        raise ValueError("Number must be between 1 and 999 inclusive.")

    # Determine the ordinal suffix
    if 11 <= value % 100 <= 13:
        return "th"
    last_digit = value % 10
    if last_digit == 1:
        return "st"
    if last_digit == 2:
        return "nd"
    if last_digit == 3:
        return "rd"
    return "th"


def line_up(name: str, number: int) -> str:
    """Formats a sentence announcing a customer's position in line.

    Args:
        name (str): The customer's name.
        number (int): The customer's position in line (1 to 999).
    Returns:
        str: A formatted string announcing the customer's position in line.
    """
    suffix = get_ordinal_suffix(number)
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
