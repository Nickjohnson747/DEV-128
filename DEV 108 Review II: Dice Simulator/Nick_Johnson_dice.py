"""
Assignment: Dice Simulator
Class: DEV 128
Date: 01/04/24
Author: Nick Johnson
Description: Program to simulate n number dice rolls
"""
import random


def display_header() -> None:
    print("=" * 30)
    print("Welcome to the Dice Roller\n")
    print("=" * 30)


def roll() -> int:
    return random.randrange(1, 7)


def roll_dice(num_rolls: int) -> list[int]:
    """
    Calls the roll function num_rolls times

    Returns:
        results (list[int]): A list of all results from rolling the dice
    """
    results: list[int] = []

    for i in range(1, num_rolls + 1):
        roll_result: int = roll()
        print("Die " + str(i) + ": " + str(roll_result))
        results.append(roll_result)

    print("-" * 17)

    return results


def get_positive_count() -> int:
    """
    Verifies that the number of times to roll is a positive integer greater than 0

    Returns:
        num_rolls (int): Number of times to roll the dice
    """
    num_rolls: int = 0

    while num_rolls < 1:
        try:
            num_rolls = int(input("Enter the number of dice to roll: "))
            if num_rolls < 1:
                print("Please enter a number greater than 0")
        except ValueError:
            print("Please enter an integer value")

    return num_rolls


if __name__ == "__main__":
    display_header()
    again: str = ""

    while again != "n".casefold():
        num_rolls = get_positive_count()
        results = roll_dice(num_rolls)
        all_same = True
        sum = 0
        start_num = results[0]

        for num in results:
            if len(results) > 1 and num != start_num or len(results) == 1:
                all_same = False
            sum += num

        print("Total:", sum)

        if all_same == True:
            print("Yay! All rolls were the same!")

        num_sixes = results.count(6)
        if num_sixes > 0:
            print("Got 6 in", str(num_sixes), "roll(s).")
        else:
            print("Sorry! No 6 found!")

        print("=" * 30)

        while again != "y".casefold() or again != "n".casefold():  # exit control flow
            again = input("Roll again? (y/n): ")
            if again == "n".casefold():
                break
            elif again == "y".casefold():
                print()
                break
