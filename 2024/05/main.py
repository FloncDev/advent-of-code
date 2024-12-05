from functools import cmp_to_key
from sys import stdin

rules, updates = [i.split("\n") for i in stdin.read().split("\n\n")]

rule_indexes = {page: [] for page in set(i.split("|")[0] for i in rules)}
for rule in rules:
    before, after = rule.split("|")
    rule_indexes[before].append(after)

total = 0
incorrect_total = 0


def compare(x, y):
    if y in rule_indexes.get(x, []):
        return 1

    elif x in rule_indexes.get(y, []):
        return -1

    return 0


for update in updates:
    if update == "":
        continue

    update = update.split(",")
    indexes = dict((i, update.index(i)) for i in update)

    valid = True
    for page in update:
        if not valid:
            break

        for page_after in rule_indexes.get(page, []):
            index = indexes.get(page_after, 9999)

            if index is None:
                continue

            if indexes[page] > index:
                valid = False
                break

    if valid:
        total += int(update[len(update) // 2])
        continue

    update.sort(key=cmp_to_key(compare), reverse=True)

    incorrect_total += int(update[len(update) // 2])

# 6138 Too low
print(total, incorrect_total)
