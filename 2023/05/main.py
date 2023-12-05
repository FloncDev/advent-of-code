#!/bin/python3
import re
from sys import stdin

raw_maps = [i.strip() for i in stdin.read().split("\n\n")]
raw_seeds = raw_maps.pop(0)

seeds = [int(i) for i in re.findall(r"\d+", raw_seeds)]

maps = []
for map in raw_maps:
    current_map = []

    for _range in map.split("\n")[1::]:
        dest, source, length = [int(i) for i in _range.split(" ")]
        current_map.append([source, source + length, dest])

    maps.append(current_map)

# Part 1
numbers = []
for index, seed in enumerate(seeds):
    current_number = seed
    for map in maps:
        for start, fin, dest in map:
            if current_number >= start and current_number < fin:
                current_number = dest + (current_number - start)
                break

    numbers.append(current_number)

seeds = []
split_seeds = raw_seeds.split(": ")[1].split(" ")
print(split_seeds, len(split_seeds))
for i in range(0, len(split_seeds), 2):
    pass

print(seeds)

print(min(numbers))
