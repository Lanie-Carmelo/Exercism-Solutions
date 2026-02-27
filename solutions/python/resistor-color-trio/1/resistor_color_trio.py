"""Resistor Color Trio This module implements the solution to the Exercism problem
"Resistor Color Trio".

The problem requires determining the value of a resistor based on its color bands. Each
color corresponds to a specific digit, and the value is calculated by combining these
digits and applying a multiplier based on the third color band.
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

PREFIXES = {
    1000000000: "gigaohms",
    1000000: "megaohms",
    1000: "kiloohms",
    1: "ohms",
}


def first_two(colors: list[str]) -> int:
    """Return the two-digit resistor value based on the first two color bands."""
    if len(colors) < 2:
        raise ValueError(
            "At least two color bands are required to determine the resistor value."
        )
    first, second = colors[:2]
    return COLOR_BANDS[first] * 10 + COLOR_BANDS[second]


def multiplier(colors: list[str]) -> int:
    """Return the multiplier based on the third color band."""
    if len(colors) < 3:
        raise ValueError(
            "At least three color bands are required to determine the multiplier."
        )
    third = colors[2]
    return 10 ** COLOR_BANDS[third]


def label(colors: list[str]) -> str:
    """Return the resistor value as a string with appropriate units (ohms, kiloohms,
    megaohms, gigaohms)."""
    value = first_two(colors) * multiplier(colors)
    for prefix_value, prefix_name in PREFIXES.items():
        if value >= prefix_value:
            return f"{value // prefix_value} {prefix_name}"
    return "0 ohms"
