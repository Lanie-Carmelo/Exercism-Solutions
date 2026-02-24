"""
Determine if a triangle is equilateral, isosceles, scalene, or degenerate.
"""

def normalized_sides(sides: list[int]) -> tuple[int, int, int]:
    """
    Normalize the sides of a triangle by making sure there are exactly 3 sides and sorting them in increasing order. This allows for easier comparison and validation.
    Args:
        sides (list[int]): The lengths of the sides of the triangle.
    Raises:
        ValueError: If there are not exactly three side lengths.
    Returns:
        tuple[int, int, int]: The lengths of the sides of the triangle, sorted in increasing order.
    """
    if len(sides) != 3:
        raise ValueError("Exactly three sides are required.")
    return tuple(sorted(sides))

def is_valid_triangle(a: int, b: int, c: int) -> bool:
    """ 
    Check if the sides of a triangle satisfy the triangle inequality and are positive.
    Args:
        a (int): The length of the shortest side of the triangle.
        b (int): The length of the middle side of the triangle.
        c (int): The length of the longest side of the triangle.
    Returns:
        bool: True if the triangle is valid, False otherwise.
    """
    return a > 0 and a + b > c

def equilateral(sides: list[int]) -> bool:
    """
    Determine if a triangle is equilateral. Uses normalized sides because if all sides are equal, triangle inequality is automatically satisfied.
    Args:
        sides (list[int]): The lengths of the sides of the triangle.
    Raises:
        ValueError: If there are not exactly three side lengths.
    Returns:
        bool: True if the triangle is equilateral, False otherwise.
    """
    a, b, c = normalized_sides(sides)
    return is_valid_triangle(a, b, c) and a == b == c

def isosceles(sides: list[int]) -> bool:
    """
    Determine if a triangle is isosceles.
    Args:
        sides (list[int]): The lengths of the sides of the triangle.
    Raises:
        ValueError: If there are not exactly three side lengths.
    Returns:
        bool: True if the triangle is isosceles, False otherwise.
    """
    a, b, c = normalized_sides(sides)
    return is_valid_triangle(a, b, c) and (a == b or b == c)

def scalene(sides: list[int]) -> bool:
    """
    Determine if a triangle is scalene.
    Args:
        sides (list[int]): The lengths of the sides of the triangle.
    Raises:
        ValueError: If there are not exactly three side lengths.
    Returns:
        bool: True if the triangle is scalene, False otherwise.
    """
    a, b, c = normalized_sides(sides)
    return is_valid_triangle(a, b, c) and len({a, b, c}) == 3

def degenerate(sides: list[int]) -> bool:
    """
    Determine if a triangle is degenerate.
    Args:
        sides (list[int]): The lengths of the sides of the triangle.
    Raises:
        ValueError: If there are not exactly three side lengths.
    Returns:
        bool: True if the triangle is degenerate, False otherwise.
    """
    a, b, c = normalized_sides(sides)
    return a > 0 and a + b == c
