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
    """Calculate the value of a resistor based on its color bands.

    Args:
        colors (str): A list of two strings representing the colors of the resistor bands.

    Returns:
        int: An integer representing the value of the resistor.
    """
    return COLOR_BANDS[colors[0]] * 10 + COLOR_BANDS[colors[1]]
