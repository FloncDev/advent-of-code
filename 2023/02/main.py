#!/bin/python3
from sys import stdin

COLOUR_MAP = {"red": 0, "green": 1, "blue": 2}

total = 0
total_power = 0

for index, line in enumerate(stdin.readlines()):
    games_str = line.strip().split(": ")[1].split("; ")
    games: list[tuple[int]] = []

    largest = [0, 0, 0]

    for game in games_str:
        cubes = game.split(", ")
        for cube in cubes:
            amount, colour = cube.split(" ")
            colour_index = COLOUR_MAP[colour]

            largest[colour_index] = max(int(amount), largest[colour_index])

    for cube, max_amount in zip(largest, [12, 13, 14]):
        if cube > max_amount:
            break
    else:
        total += index + 1

    total_power += largest[0] * largest[1] * largest[2]

print(total)
print(total_power)
