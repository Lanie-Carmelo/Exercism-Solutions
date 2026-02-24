"""Calculates the score for a dart throw.

- If the dart lands outside the target, player earns no points (0 points).
- If the dart lands in the outer circle of the target, player earns 1 point.
- If the dart lands in the middle circle of the target, player earns 5 points.
- If the dart lands in the inner circle of the target, player earns 10 points.
"""

BANDS = ((1**2, 10), (5**2, 5), (10**2, 1))  # Ordered from smallest radius to largest


def score(x_coord: float, y_coord: float) -> int:
    """Calculate the score for a dart throw.

    Args:
        x_coord (float): The x coordinate of the dart throw.
        y_coord (float): The y coordinate of the dart throw.
    Returns:
        int: The score for the dart throw.
    """
    distance_squared = x_coord**2 + y_coord**2
    for limit, points in BANDS:
        if distance_squared <= limit:
            return points
    return 0
