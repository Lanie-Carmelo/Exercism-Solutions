"""All Your Base.

Given a number in base `input_base` represented as a sequence of digits, convert it to base `output_base` and return the result as a sequence of digits.
"""

from collections.abc import Sequence


def _to_decimal(input_base: int, digits: Sequence[int]) -> int:
    """Convert a number from a given base to decimal.

    Args:
        input_base: The base of the input number.
        digits: The digits of the input number, in order from most significant to least significant. An empty digit sequence represents 0.

    Returns:
        The decimal representation of the input number.
    """
    value = 0
    for digit in digits:
        value = value * input_base + digit
    return value


def _from_decimal(number: int, output_base: int) -> list[int]:
    """Convert a number from decimal to a given base.

    Args:
        number: The decimal representation of the input number.
        output_base: The base of the output number.
    Returns:
        The digits of the output number, in order from most significant to least significant.
    """
    if number == 0:
        return [0]
    out_digits: list[int] = []
    while number > 0:
        number, remainder = divmod(number, output_base)
        out_digits.append(remainder)
    return list(reversed(out_digits))


def rebase(input_base: int, digits: Sequence[int], output_base: int) -> list[int]:
    """Convert a number from one base to another.

    Args:
        input_base: The base of the input number.
        digits: The digits of the input number, in order from most significant to least significant.
        output_base: The base of the output number.

    Returns:
        The digits of the output number, in order from most significant to least significant.
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    decimal_value = _to_decimal(input_base, digits)
    return _from_decimal(decimal_value, output_base)
