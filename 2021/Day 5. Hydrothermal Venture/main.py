import re
from collections import Counter


with open("input.txt", "r") as f:
    coord_init = [re.split(' -> |,', line.rstrip()) for line in f]


def part1():
    coord = []
    for c in coord_init:
        x1, y1, x2, y2 = [int(num) for num in c]
        # horizontal
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                coord.append((x1, i))
        # vertical
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                coord.append((i, y2))
    return count(coord)


def part2():
    coord = []
    for c in coord_init:
        x1, y1, x2, y2 = [int(num) for num in c]
        # horizontal
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                coord.append((x1, i))
        # vertical
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                coord.append((i, y2))
        # diagonal
        else:
            x_inc = 1 if x1 < x2 else -1
            y_inc = 1 if y1 < y2 else -1
            y = y1
            for x in range(x1, x2+x_inc, x_inc):
                coord.append((x, y))
                y += y_inc
    return count(coord)


def count(coord):
    return len([c for c in Counter(coord).values() if c >= 2])


print(part1())
print(part2())
