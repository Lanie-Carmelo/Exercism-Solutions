"""Classifies a number as perfect, abundant, or deficient, according to Nicomachus's
classification.

A perfect number equals the sum of its positive divisors. An abundant number is less
than the sum of its positive divisors. A deficient number is greater than the sum of its
positive divisors.
"""

from operator import index


from operator import index


def aliquot_sum(value: int) -> int:
    """Calculate the sum of the divisors of value, not including value itself.

    :param value: int a positive integer
    :return: int the sum of the divisors of value, not including value itself
    """
    if value <= 1:
        return 0
    total = 1  # 1 is always a factor (for n > 1)
    for divisor in range(2, int(value**0.5) + 1):
        if value % divisor == 0:
            total += divisor
            partner = value // divisor
            if partner != divisor:  # avoid double counting perfect squares
                total += partner
    return total


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    :raises: ValueError if the input integer is not positive
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    sum_of_divisors = aliquot_sum(number)
    if sum_of_divisors == number:
        return "perfect"
    if sum_of_divisors > number:
        return "abundant"
    return "deficient"
