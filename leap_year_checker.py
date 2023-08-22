"""
This program contains a function that checks
if a given year is a leap year or not.
"""

def is_leap_year(year: int) -> bool:
    """
    Verifies if the given year is a leap year or not

    Args: 
        year - given year
    
    Return:
        A boolean value: True if it is a leap year; False if not a leap year
    """
    if (year % 100 != 0):
        leap_year = year % 4 == 0
    if (year % 100 == 0):
        leap_year = year % 400 == 0
    
    return leap_year

def main():
    year = int(input("Enter a year to be checked if leap year or not: "))
    
    leap_year_check = is_leap_year(year)

    if leap_year_check:
        print(f"{year} is a leap year.")
    if not leap_year_check:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
