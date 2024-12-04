from sys import stdin

data = stdin.readlines()

total = 0

for y, line in enumerate(data):
    for x, char in enumerate(line.strip()):
        if char != "A":
            continue

        if x == 0 or y == 0:
            continue

        try:
            if "".join(
                [
                    data[y - 1][x - 1],
                    data[y - 1][x + 1],
                    data[y + 1][x - 1],
                    data[y + 1][x + 1],
                ]
            ) in ["MSMS", "SMSM", "SSMM", "MMSS"]:
                total += 1
        except IndexError:
            pass

print(total)
