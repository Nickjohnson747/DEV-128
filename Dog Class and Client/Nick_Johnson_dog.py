"""
Assignment: Dog Class and Client
Class: DEV 128
Date: 01/18/24
Author: Nick Johnson
Description: Creates a dog and allows users to interact with it
    Supports
        Getting the status of a dog,
        Feeding a dog,
        Walking the dog.
"""


class Dog:
    def __init__(self, name: str, color: str, weight: float = 10.0) -> None:
        self.name = name.title()
        self.color = color.title()
        self.weight = weight
        self.isHungry = True

    def bark(self) -> None:
        print(self.name, ": Woof Woof")

    def eat(self) -> None:
        # will still add weight if dog isn't hungry and user uses feed command
        self.isHungry = False
        self.weight += 0.1
        print(self.name, ": Chomp Chomp")

    def walk(self) -> None:
        if self.isHungry == True:
            self.bark()
        else:
            self.weight -= 0.1
            self.isHungry = True
            print(self.name, ": Step Step")

    def printStatus(self) -> None:
        prnt_string: str = (
            self.name
            + " is "
            + self.color
            + " in color, weighs "
            + str(format(self.weight, ".1f"))
            + " kg and is "
        )

        if self.isHungry == True:
            prnt_string += "hungry."
        else:
            prnt_string += "not hungry."

        print(prnt_string)


def main():
    dog = Dog(name="Willie", color="Brown", weight=15)
    print(dog.name, "welcomes you! Woof Woof")

    while True:
        print("-" * 42)
        print("Enter the command:")
        print("'S' to get status enquiry,\t\t 'F' to feed the dog")
        print("'W' to take it for a walk,\t\t 'Q' to exit:")
        command: str = input().upper()

        if command == "S":
            dog.printStatus()
        elif command == "F":
            dog.eat()
        elif command == "W":
            dog.walk()
        elif command == "Q":
            print("Goodbye! Woof Woof")
            break


if __name__ == "__main__":
    main()
