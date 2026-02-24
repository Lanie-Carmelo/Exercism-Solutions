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

def is_valid_triangle(shortest: int, middle: int, longest: int) -> bool:
    """ 
    Check if the sides of a triangle satisfy the triangle inequality and are positive.
    Args:
        shortest (int): The length of the shortest side of the triangle.
        middle (int): The length of the middle side of the triangle.
        longest (int): The length of the longest side of the triangle.
    Returns:
        bool: True if the triangle is valid, False otherwise.
    """
    return shortest > 0 and shortest + middle > longest

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
    shortest, middle, longest = normalized_sides(sides)
    return is_valid_triangle(shortest, middle, longest) and shortest == middle == longest

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
    shortest, middle, longest = normalized_sides(sides)
    return is_valid_triangle(shortest, middle, longest) and middle in (shortest, longest)

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
    shortest, middle, longest = normalized_sides(sides)
    return is_valid_triangle(shortest, middle, longest) and len({shortest, middle, longest}) == 3

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
    shortest, middle, longest = normalized_sides(sides)
    return shortest > 0 and shortest + middle == longest
