from sys import stdin

list_1 = []
list_2 = []

for index, line in enumerate(stdin.readlines()):
    values = line.strip().split()
    list_1.append(int(values[0]))
    list_2.append(int(values[1]))

total_distance = 0

for left, right in zip(sorted(list_1), sorted(list_2)):
    total_distance += abs(left - right)

similarity = 0

for left in list_1:
    similarity += list_2.count(left) * left

print(total_distance, similarity)
