"""Converts a number to its raindrop sound.

If the number contains 3 as a factor, add 'Pling' to the result. If the number contains
5 as a factor, add 'Plang' to the result. If the number contains 7 as a factor, add
'Plong' to the result. If the number does not contain 3, 5, or 7 as a factor, the result
should be the digits of the number.
"""


def convert(number: int) -> str:
    """Convert a number to a string of raindrop sounds.

    Args:
        number (int): The number to convert.
    Returns:
        str: The raindrop sound string.
    """
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    return result or str(number)
