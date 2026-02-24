"""Calculates the score for a dart throw.

- If the dart lands outside the target, player earns no points (0 points).
- If the dart lands in the outer circle of the target, player earns 1 point.
- If the dart lands in the middle circle of the target, player earns 5 points.
- If the dart lands in the inner circle of the target, player earns 10 points.
"""


def score(x_coord: int, y_coord: int) -> int:
    """Calculate the score for a dart throw.

    Args:
        x_coord: The x coordinate of the dart throw.
        y_coord: The y coordinate of the dart throw.
    Returns:
        int: The score for the dart throw.
    """
    distance_squared = x_coord**2 + y_coord**2
    inner_circle_radius = 1
    middle_circle_radius = 5
    outer_circle_radius = 10
    if distance_squared <= inner_circle_radius**2:
        return 10
    if distance_squared <= middle_circle_radius**2:
        return 5
    if distance_squared <= outer_circle_radius**2:
        return 1
    return 0
