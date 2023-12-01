import numpy as np
from statistics import median


with open("input.txt", "r") as f:
    positions = sorted(list(map(int, f.readline().split(','))))


def part1():
    # the closest position is the median
    med = int(median(positions))  # np.median(positions)
    return sum([abs(num - med) for num in positions])


def triangular_cost(steps):
    return steps * (steps + 1) // 2


def part2():
    mean = int(np.mean(positions))
    return sum([triangular_cost(abs(num - mean)) for num in positions])


print(part1())
print(part2())
