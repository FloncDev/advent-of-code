#!/usr/bin/python3
import re
from math import lcm
from sys import stdin

LR_LOOKUP = {"L": "left", "R": "right"}


class Node:
    def __init__(self, line: str) -> None:
        nodes = re.search(r"\((.*?)\)", line).group(1).split(", ")
        self.node = line[0:3]
        self.left = nodes[0]
        self.right = nodes[1]

    def __str__(self) -> str:
        return f"{self.node} -> {self.left} {self.right}"

    def __repr__(self) -> str:
        return self.__str__()


search_pattern = stdin.readline().strip()

nodes = {}

for line in stdin.readlines()[1::]:
    node = Node(line)
    nodes[node.node] = node

# steps = 0
# current_node = nodes["AAA"]
# while True:
#     if current_node.node == "ZZZ":
#         break

#     instruction = search_pattern[steps % len(search_pattern)]

#     match instruction:
#         case "L":
#             current_node = nodes[current_node.left]

#         case "R":
#             current_node = nodes[current_node.right]

#     steps += 1

ghost_steps = 0
current_nodes: list[Node] = []

for node in nodes.values():
    if node.node.endswith("A"):
        current_nodes.append(node)

loop_counts = [0 for _ in current_nodes]
finished = 0

while True:
    instruction = LR_LOOKUP[search_pattern[ghost_steps % len(search_pattern)]]

    for index, node in enumerate(current_nodes):
        if loop_counts[index] != 0:
            continue

        if node.node.endswith("Z"):
            finished += 1
            loop_counts[index] = ghost_steps
            continue

        current_nodes[index] = nodes[current_nodes[index].__getattribute__(instruction)]

    if finished == len(current_nodes):
        break

    ghost_steps += 1

print(ghost_steps)
print(lcm(*loop_counts))
# print(steps)
