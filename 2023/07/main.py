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

        self.get_strength(self.cards)

    def get_strength(self, cards):
        counted = {}
        for card in cards:
            if card in counted:
                continue

            counted[card] = cards.count(card)

        counted = dict(sorted(counted.items(), key=lambda i: i[1])[::-1])
        keys = list(counted.values())

        if keys[0] == 5:
            self.strength = 0
        elif keys[0] == 4:
            self.strength = 1
        elif keys[0] == 3 and keys[1] == 2:
            self.strength = 2
        elif keys[0] == 3:
            self.strength = 3
        elif keys[0] == 2 and keys[1] == 2:
            self.strength = 4
        elif keys[0] == 2:
            self.strength = 5
        else:
            self.strength = 6

        self.counted = counted

    def __str__(self):
        return f"{''.join(self.cards)}({self.strength}) {self.bet} {self.counted}"

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


cards = [Deck(i.strip()) for i in stdin.readlines()]

winnings = 0
for index, card in enumerate(sorted(cards)):
    winnings += card.bet * (index + 1)

print(winnings)
