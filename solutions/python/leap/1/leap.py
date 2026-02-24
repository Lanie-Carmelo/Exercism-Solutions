"""
Determine if a year is a leap year.
A leap year is defined as follows:
- It is evenly divisible by 4;
- Except if it is evenly divisible by 100, then it is not a leap year;
- Except if it is evenly divisible by 400, then it is a leap year.
"""


def leap_year(year):
    """Function to determine if a given year is a leap year.

    Args:
        year (int): The year to check.
    Returns:
        bool: True if the year is a leap year, False otherwise.
    """    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
