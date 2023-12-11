#!/bin/python3
from sys import stdin

from rich import print

# Index [y][x]
pipes = stdin.read().translate(str.maketrans("-|F7LJ.", "─│┌┐└┘ ")).split("\n")

# [north, south, east, west]
pipe_map = {
    #     0  1  2  3
    "─": [0, 0, 1, 1],
    "│": [1, 1, 0, 0],
    "┌": [0, 1, 1, 0],
    "┐": [0, 1, 0, 1],
    "└": [1, 0, 1, 0],
    "┘": [1, 0, 0, 1],
    "S": [1, 1, 1, 1],
    " ": [0, 0, 0, 0],
}

connection_map = {0: 1, 1: 0, 2: 3, 3: 2}

NORTH = (1, 0)
SOUTH = (-1, 0)
EAST = (0, 1)
WEST = (0, -1)


def find_connecting(y, x) -> tuple[tuple[int, int], tuple[int, int]]:
    pipe_connects_to = pipe_map[pipes[y][x]]

    connecting = []
    for index, (delta_y, delta_x) in enumerate([NORTH, SOUTH, EAST, WEST]):
        pipe_x = x + delta_x
        pipe_y = y + delta_y

        try:
            other_pipe = pipe_map[pipes[pipe_y][pipe_x]]
        except IndexError:
            continue

        if pipe_connects_to == other_pipe:
            connecting.append((pipe_y, pipe_x))

        elif pipe_connects_to[index] * other_pipe[connection_map[index]] == 1:
            connecting.append((pipe_y, pipe_x))

    return (connecting[0], connecting[1])


# Find the start
start = (0, 0)

for y, row in enumerate(pipes):
    for x, tile in enumerate(row):
        if tile == "S":
            start = (y, x)
            break

loop_pipes = [start]


def find_next_pipe(y, x):
    try:
        pipe = [i for i in find_connecting(y, x) if i not in loop_pipes][0]
    except:
        return

    loop_pipes.append(pipe)
    find_next_pipe(*pipe)


find_next_pipe(*start)

out_str = [[char for char in i] for i in pipes]

for y, x in loop_pipes:
    out_str[y][x] = f"[green]{out_str[y][x]}[/green]"

print("\n".join("".join(i for i in line) for line in out_str))
