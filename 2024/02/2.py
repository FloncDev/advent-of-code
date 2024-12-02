from math import copysign
from sys import stdin

sign = lambda x: copysign(1, x)


def check_report(report: list[int]) -> bool | int:
    differences = []

    for left, right in zip(report[1:], report[:-1]):
        differences.append(left - right)

    trend = sign(sum(sign(i) for i in differences))

    for index, difference in enumerate(differences):
        if sign(difference) != trend:
            return index

        if difference == 0 or abs(difference) > 3:
            return index

    return True


safe = 0

for report in stdin.readlines():
    report = [int(i) for i in report.strip().split()]

    validity = check_report(report)

    if validity is True:
        safe += 1
        continue

    # If validity is not True, that means there was atleast 1 error.
    # At this point, create 2 copies of the report with each of the values missing
    reports = [report.copy(), report.copy()]
    [reports[i].pop(validity + i) for i in range(2)]

    for new_report in reports:
        if check_report(new_report) is True:
            safe += 1
            break

print(safe)
