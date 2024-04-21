"""
Assignment: Season calculator 
Class: DEV 128
Date: 01/03/24
Author: Nick Johnson
Description: Program to determine the season given the month and date.
"""
print("Welcome to the Seasons program")


def get_season(month: str, day: str) -> str:
    """
    Determines the season based on the given date
    """

    if (month == 12 and day >= 16) or month in [1, 2] or (month == 3 and day <= 15):
        return "Winter"

    elif (month == 3 and day >= 16) or month in [4, 5] or (month == 6 and day <= 15):
        return "Spring"

    elif (month == 6 and day >= 16) or month in [7, 8] or (month == 9 and day <= 15):
        return "Summer"

    elif (month == 9 and day >= 16) or month in [10, 11] or (month == 12 and day <= 15):
        return "Fall"

    return "Unable to determine season"


months: list[int] = list(range(1, 13))
long_months: list[int] = [1, 3, 5, 7, 8, 10, 12]  # 31 day months
short_months: list[int] = [4, 6, 9, 11]  # 30 day months

again: str = ""

while again != "n".casefold():
    month: int = -1
    day: int = -1
    season: str = ""

    while month < 1 or month > 12:
        month = int(input("Please enter the month (1-12): "))

        if month not in months:
            print("Invalid month entered")

    if month in months and month in long_months:
        while day < 1 or day > 31:
            day = int(input("Please enter the day (1-31): "))
            if not (0 < day < 32):
                print("Invalid day entered")
            else:
                season = get_season(month, day)
    elif month in months and month in short_months:
        while day < 1 or day > 30:
            day = int(input("Please enter the day (1-30): "))
            if not (0 < day < 31):
                print("Invalid day entered")
            else:
                season = get_season(month, day)
    elif month == 2:  # February case
        while day < 1 or day > 28:
            day = int(input("Please enter the day (1-28): "))
            if not (0 < day < 29):
                print("Invalid day entered")
            else:
                season = get_season(month, day)
    print("Season = " + season)

    while again != "y".casefold() or again != "n".casefold():  # exit control flow
        again = input("Would you like to enter another date? (y/n): ")
        if again == "n".casefold():
            print("Goodbye!")
            break
        elif again == "y".casefold():
            break
