from itertools import pairwise

from utils.measure import timeit


def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
        return [list(map(int, line.split())) for line in lines]


def get_total(data, reverse=False):
    total = 0

    for row in data:
        if reverse:
            row = row[::-1]

        diff = row
        total += diff[-1]

        while not all(value == 0 for value in diff):
            diff = [y - x for x, y in pairwise(diff)]
            total += diff[-1]

    return total


@timeit
def part1(data):
    return get_total(data)


@timeit
def part2(data):
    return get_total(data, True)


if __name__ == '__main__':
    print(part1(read_file('test.txt')))
    print(part1(read_file('input.txt')))
    print(part2(read_file('test.txt')))
    print(part2(read_file('input.txt')))
