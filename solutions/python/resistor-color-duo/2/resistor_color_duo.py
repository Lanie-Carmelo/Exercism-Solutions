"""Resistor Color Duo.

This module implements the solution to the Exercism problem "Resistor Color Duo". The
problem requires determining the value of a resistor based on its color bands. Each
color corresponds to a specific digit, and the value is calculated by combining these
digits.
"""

COLOR_BANDS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def value(colors: list[str]) -> int:
    """Return the two-digit resistor value based on the first two color bands.

    Args:
        colors (list[str]): A list of strings representing the resistor bands.

    Returns:
        int: An integer representing the value of the resistor.
    """
    if len(colors) < 2:
        raise ValueError(
            "At least two color bands are required to determine the resistor value."
        )
    first, second = colors[:2]
    return COLOR_BANDS[first] * 10 + COLOR_BANDS[second]
