#!/bin/python3
import functools
from sys import stdin

rankings = [i for i in "23456789TJQKA"]


@functools.total_ordering
class Deck:
    def __init__(self, line: str) -> None:
        self.line = line.split(" ")
        self.cards = [i for i in self.line[0]]
        self.bet = int(self.line[1])

        strength_return = self.get_strength(self.cards)
        self.strength = strength_return[0]
        self.counted = strength_return[1]

    def convert_Js(self):
        joker_count = self.counted.get("J", 0)

        if joker_count == 0:
            return

        # Change jokers to highest best cards
        for card in self.counted.keys():
            if card == "J":
                continue

            del self.counted["J"]
            self.counted[card] = self.counted[card] + joker_count
            break

        joker_cards = []
        for card, amount in self.counted.items():
            [joker_cards.append(card) for i in range(amount)]

        self.cards = joker_cards

        self.strength, _ = self.get_strength(self.cards)

    def count_cards(self, cards):
        counted = {}
        for card in cards:
            if card in counted:
                continue

            counted[card] = cards.count(card)

        counted = dict(sorted(counted.items(), key=lambda i: i[1])[::-1])
        return counted

    def get_strength(self, cards):
        counted = self.count_cards(cards)
        keys = list(counted.values())
        strength = 0

        if keys[0] == 5:
            strength = 0
        elif keys[0] == 4:
            strength = 1
        elif keys[0] == 3 and keys[1] == 2:
            strength = 2
        elif keys[0] == 3:
            strength = 3
        elif keys[0] == 2 and keys[1] == 2:
            strength = 4
        elif keys[0] == 2:
            strength = 5
        else:
            strength = 6

        return strength, counted

    def __str__(self):
        return f"{''.join(self.cards)}({self.strength}) {self.bet}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: "Deck"):
        return self.counted == other.counted

    def __gt__(self, other: "Deck"):
        if self.strength != other.strength:
            return self.strength < other.strength

        for self_card, other_card in zip(self.cards, other.cards):
            if self_card == other_card:
                continue

            return rankings.index(self_card) > rankings.index(other_card)


decks = [Deck(i.strip()) for i in stdin.readlines()]

winnings = 0
for index, card in enumerate(sorted(decks)):
    winnings += card.bet * (index + 1)

rankings = [i for i in "J23456789TQKA"]
[i.convert_Js() for i in decks]

joker_winnings = 0
for index, card in enumerate(sorted(decks)):
    joker_winnings += card.bet * (index + 1)

print(winnings)
print(joker_winnings, decks)
