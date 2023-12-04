#!/bin/python3
from sys import stdin

total = 0
cards = {}

for index, line in enumerate(stdin.readlines()):
    cards[index + 1] = cards.get(index + 1, 0) + 1  # The original card

    winning, card = line.strip().split(": ")[1].split("|")

    winning_numbers = set(int(i) for i in winning.strip().split(" ") if i != "")
    card_numbers = set(int(i) for i in card.strip().split(" ") if i != "")

    points = 0
    cards_won = 0

    for winning_number in winning_numbers:
        if winning_number in card_numbers:
            points = 1 if not points else points * 2
            cards_won += 1

    total += points

    for i in range(index + 2, (index + 1) + cards_won + 1):
        cards[i] = cards.get(i, 0) + cards[index + 1]

print(total)
print(sum(i for i in cards.values()))
