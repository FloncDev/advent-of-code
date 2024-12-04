from sys import stdin

data = stdin.readlines()


def check_letter(
    x: int,
    y: int,
    letters: list[str],
    d: tuple[int, int] | tuple[None, None] = (None, None),
) -> int:
    if x >= len(data[0]) or x < 0 or y >= len(data) or y < 0:
        return 0

    if data[y][x] != letters[0]:
        return 0

    if len(letters) == 1:
        return 1

    count = 0

    if d == (None, None):
        for dx in range(-1, 2, 1):
            for dy in range(-1, 2, 1):
                if (dx, dy) == (0, 0):
                    continue

                if y + dy in [-1, len(data)] or x + dx in [-1, len(data[0])]:
                    continue

                count += check_letter(x + dx, y + dy, letters[1:], (dx, dy))

    else:
        count += check_letter(x + d[0], y + d[1], letters[1:], d)

    return count


total = 0

for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "X":
            total += check_letter(x, y, [i for i in "XMAS"])

print(total)
