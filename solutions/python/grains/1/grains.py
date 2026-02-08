"""
Functions to determine the number of grains of wheat on one square of a chessboard and on the board as a whole. Each square has double the previous square's amount, starting with 1 grain on the first square.
"""


def square(number):
    """
    Returns the number of grains on a given square of a chessboard.
    If the square number is out of range, not between 1 and 64 inclusive, a ValueError exception is thrown.

    Param number: int - Number of square to check for amount of grains
    Return: int - Number of grains on given square
    """

    # Raise exception if square number is not between 1 and 64, the amount of squares on a chessboard.
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number - 1)


def total():
    """
    Calculates the total number of grains of wheat on the whole chessboard

    Return: int - total number of grains
    """

    total_grains = 0
    for i in range(1, 65):
        total_grains += square(i)
    return total_grains
