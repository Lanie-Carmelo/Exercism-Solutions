"""
Determine if a year is a leap year.
A leap year is defined as follows:
- It is evenly divisible by 4;
- Except if it is evenly divisible by 100, then it is not a leap year;
- Except if it is evenly divisible by 400, then it is a leap year.
"""


def leap_year(year: int) -> bool:
    """Function to determine if a given year is a leap year.

    Args:
        year (int): The year to check.
    Returns:
        bool: True if the year is a leap year, False otherwise.
    """    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
