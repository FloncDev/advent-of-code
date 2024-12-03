import re
from sys import stdin

total = 0
p2_total = 0
enabled = True

for match in re.finditer(r"(?:mul\((\d+),(\d+)\))|don\'t\(\)|do\(\)", stdin.read()):
    match match.group(0):
        case "do()":
            enabled = True

        case "don't()":
            enabled = False

        case _:
            mult = int(match.group(1)) * int(match.group(2))
            total += mult

            if enabled:
                p2_total += mult

print(total, p2_total)
