"""Classifies a number as perfect, abundant, or deficient, according to Nicomachus's
classification.

A perfect number equals the sum of its positive divisors. An abundant number is less
than the sum of its positive divisors. A deficient number is greater than the sum of its
positive divisors.
"""


def aliquot_sum(number: int) -> int:
    """Calculate the sum of the divisors of n, not including n itself.

    :param number: int a positive integer
    :return: int the sum of the divisors of n, not including n itself
    """
    if number <= 1:
        return 0
    total = 1  # 1 is always a factor (for n > 1)
    for index in range(2, int(number**0.5) + 1):
        if number % index == 0:
            total += index
            partner = number // index
            if partner != index:  # avoid double counting perfect squares
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
