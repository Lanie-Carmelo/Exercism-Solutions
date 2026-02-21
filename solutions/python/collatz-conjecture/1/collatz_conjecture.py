"""Collatz Conjecture"""

def steps(number):
    """
    Calculate the number of steps required to reach 1.

    param number - int: A positive integer
    return -int: The number of steps required to reach 1
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
    count = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        count += 1
    return count
