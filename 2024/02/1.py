from sys import stdin

safe = 0

for report in stdin.readlines():
    report = [int(i) for i in report.strip().split()]

    is_increasing = None

    for val, prev in zip(report[1:], report[:-1]):
        # Diff less than 1
        if val == prev:
            break

        difference = prev - val

        # Diff more than 3
        if abs(difference) > 3:
            break

        if is_increasing is None:
            is_increasing = difference > 0

        # Pattern changed
        if is_increasing and difference < 0:
            break
        elif not is_increasing and difference > 0:
            break

    else:
        safe += 1

print(safe)
