from math import prod


def slope_count(slope):
    count = i = j = 0
    while i < len(trees):
        if trees[i][j % len(trees[0])] == '#':
            count += 1
        i += slope[1]  # down
        j += slope[0]  # right
    return count


with open('trees.txt', 'r') as f:
    trees = [line.strip() for line in f.readlines()]

print(slope_count([3, 1]))
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print(prod(slope_count(slope) for slope in slopes))
