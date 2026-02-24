"""Calculates the score for a dart throw.

- If the dart lands outside the target, player earns no points (0 points).
- If the dart lands in the outer circle of the target, player earns 1 point.
- If the dart lands in the middle circle of the target, player earns 5 points.
- If the dart lands in the inner circle of the target, player earns 10 points.
"""

INNER = 1
MIDDLE = 25
OUTER = 100


def score(x_coord: float, y_coord: float) -> int:
    """Calculate the score for a dart throw.

    Args:
        x_coord (float): The x coordinate of the dart throw.
        y_coord (float): The y coordinate of the dart throw.
    Returns:
        int: The score for the dart throw.
    """
    distance_squared = x_coord**2 + y_coord**2
    if distance_squared <= INNER:
        return 10
    if distance_squared <= MIDDLE:
        return 5
    if distance_squared <= OUTER:
        return 1
    return 0
