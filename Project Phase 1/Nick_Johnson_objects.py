#!/usr/bin/env python3
"""
Assignment: Final Project
Class: DEV 128
Date: 02/21/2024
Author: Nick Johnson
Description: Program to simulate Blackjack
"""
import random
import copy

CARDS_CHARACTERS = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}


##########################################################################
## Definitions for the classes: Card, Deck and Hand
##########################################################################
class Card:
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self, rank: str, suit: str):
        if rank not in Card.RANKS:
            raise ValueError(
                "Card rank must be 'Ace', 2-10, 'Jack', 'Queen', or 'King'"
            )
        else:
            self.__rank = rank

        if suit not in CARDS_CHARACTERS.keys():
            raise ValueError("Suit must be 'Spades', 'Hearts', 'Diamonds', or 'Clubs'")
        else:
            self.__suit = suit

    @property  # read-only
    def value(self) -> int:
        """
        Converts a cards rank to the corresponding 1-11 value
        """
        if self.__rank == "Ace":
            return 11
        elif self.__rank == "Jack" or self.__rank == "Queen" or self.__rank == "King":
            return 10
        else:
            return int(self.__rank)

    def displayCard(self) -> str:
        return self.__rank + " of " + self.__suit + " " + CARDS_CHARACTERS[self.__suit]


class Deck:
    def __init__(self):
        suits = CARDS_CHARACTERS.keys()
        ranks = Card.RANKS
        self.__deck = []

        for suit in suits:
            for rank in ranks:
                self.__deck.append(Card(rank, suit))

    @property  # read-only
    def count(self) -> int:
        return len(self.__deck)

    def shuffle(self):
        random.shuffle(self.__deck)

    def dealCard(self) -> str:
        """
        Removes a card from the deck and returns it
        """
        idx = random.randrange(0, 52)
        ret_card = copy.copy(self.__deck[idx])  # copy value to return after del
        del self.__deck[idx]

        return ret_card


class Hand:
    def __init__(self):
        self.__cards = []

    @property  # read-only
    def count(self) -> int:
        return len(self.__cards)

    @property  # read-only
    def points(self) -> int:
        total = 0
        for card in self.__cards:
            total += card.value

        return total

    def addCard(self, card: Card) -> None:
        self.__cards.append(card)

    def displayHand(self) -> None:
        for card in self.__cards:
            print(card.displayCard())


def main():
    print("Cards - Tester")
    print()

    # test deck
    print("DECK")
    deck = Deck()
    print("Deck created.")
    deck.shuffle()
    print("Deck shuffled.")
    print("Deck count:", deck.count)
    print()

    # test hand
    print("HAND")
    hand = Hand()
    for i in range(4):
        hand.addCard(deck.dealCard())

    hand.displayHand()
    print()

    print("Hand points:", hand.points)
    print("Hand count:", hand.count)
    print("Deck count:", deck.count)


if __name__ == "__main__":
    main()
