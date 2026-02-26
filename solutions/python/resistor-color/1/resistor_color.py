"""Resistor Color Codes.

This module provides a way to quickly look up the code for a resistor based on its
color.
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


def color_code(color: str) -> int:
    """Look up the value of a resistor based on its color.

    Args:
        color (str): The color of the resistor.
    Returns:
        int: The value of the resistor.
    """
    if color not in COLOR_BANDS:
        raise ValueError(f"Invalid color: {color}")
    return COLOR_BANDS[color]


def colors() -> list[str]:
    """Return a list of all the colors in the resistor color code.

    Returns:
        list[str]: A list of all the colors in the resistor color code.
    """
    return list(COLOR_BANDS.keys())
