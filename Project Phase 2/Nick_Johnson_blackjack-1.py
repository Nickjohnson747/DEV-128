#!/usr/bin/env python3
"""
Assignment: Final Project
Class: DEV 128
Date: 03/04/2024
Author: Nick Johnson
Description: Program to simulate Blackjack
"""
from Nick_Johnson_objects import Card, Deck, Hand


class Blackjack:
    def __init__(self, startingBalance: int):
        self.__money = startingBalance

    def displayCards(self, hand: Hand, title: str) -> None:
        """Print the title, print the cards and the points of the hand."""
        print(title + "\n")
        print(hand)
        print("Points: {}".format(hand.points))

        print()

    def getBet(self) -> int:
        """Method to update self.bet by prompting the user for the bet amount,
        making sure bet is less than self.money."""
        self.__bet = -1
        while self.__bet < 0 or self.__bet > self.__money:
            bet_amt = int(input("Bet amount: "))
            if bet_amt < 0:
                print("Invalid amount. Enter a positive number")
            elif bet_amt > self.__money:
                print("You don't have enough money to make that bet.")
            else:
                return bet_amt

    def setupRound(self) -> None:
        """Setup the round by doing these steps:
        initialize self.deck to a new Deck object and shuffle it
        initialize self.dealerHand and self.playerHand to new Hand objects
        deal two cards to the playerHand, and one card to the dealerHand
        finally, print dealerHand and playerHand using displayCards method."""
        self.__deck = Deck()
        self.__deck.shuffle()

        self.__dealer_hand = Hand()
        self.__dealer_hand.addCard(self.__deck.dealCard())
        self.displayCards(self.__dealer_hand, "DEALER'S SHOW CARD:")

        self.__player_hand = Hand()
        for _ in range(2):
            self.__player_hand.addCard(self.__deck.dealCard())
        self.displayCards(self.__player_hand, "YOUR CARDS:")

    def takePlayerTurn(self) -> bool:
        """Method to simulate player playing one turn by dealing a card
        to the player."""
        self.__player_hand.addCard(self.__deck.dealCard())
        self.displayCards(self.__player_hand, "YOUR CARDS:")

        return self.__player_hand.is_busted()

    @property  # read-only
    def is_busted(self) -> bool:
        return self.__player_hand.is_busted()

    @property  # read-only
    def hand_points(self) -> int:
        return self.__player_hand.points


def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    # initialize starting money
    money = 100
    print("Starting Balance:", money)
    # instantiate object of Blackjack class
    blackjack = Blackjack(money)

    print("Setting up a round...")
    print(blackjack.getBet())
    blackjack.setupRound()

    print("Playing Player Hand...")

    move = ""

    while move != "h" or move != "s":
        # properly updates points after a hit that busts
        hand_points = blackjack.hand_points
        if blackjack.is_busted:
            print("\nYOUR POINTS: {}".format(hand_points))
            break

        move = input("Hit or stand? (h for hit, s for stand): ").lower()
        if move == "h":
            blackjack.takePlayerTurn()
        elif move == "s":
            print("\nYOUR POINTS: {}".format(hand_points))
            break

    print("Good bye!")


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
