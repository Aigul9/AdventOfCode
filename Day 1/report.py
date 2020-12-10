from math import prod
from itertools import combinations


def solve(length):
    for c in combinations(n, length):
        if sum(c) == 2020:
            return prod(c)


with open('report.txt', 'r') as f:
    n = [int(line.strip()) for line in f.readlines()]

print(solve(2))
print(solve(3))
