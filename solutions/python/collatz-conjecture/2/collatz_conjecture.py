"""
Compute the number of steps required for a number to reach 1
under the Collatz process.

For a positive integer n:
- if n is even, divide it by 2
- if n is odd, multiply by 3 and add 1

The Collatz conjecture states that this process eventually
reaches 1 for all positive integers, though it remains unproven.
"""

def steps(number: int) -> int:
    """Return how many Collatz steps are needed to reach 1.

    Args:
        number: A positive integer.

    Returns:
        The number of steps in the sequence.

    Raises:
        ValueError: If number is not a positive integer.
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps_count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        steps_count += 1

    return steps_count
