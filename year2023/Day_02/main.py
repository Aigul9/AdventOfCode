from math import prod

from year2023.utils.time import timeit


CONSTRAINTS = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def check_game(subsets):
    for subset in subsets.split('; '):
        for row in subset.split(', '):
            num, color = row.split()
            num = int(num)
            if num > CONSTRAINTS[color]:
                return False
    return True


@timeit
def part1(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
        total = 0
        for line in lines:
            game, attempts = line.split(': ')
            game_num = int(game.split()[1])
            if check_game(attempts):
                total += game_num
    return total


def get_power(subsets):
    max_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for subset in subsets.split('; '):
        for row in subset.split(', '):
            num, color = row.split()
            max_cubes[color] = max(int(num), max_cubes[color])

    return prod(max_cubes.values())


@timeit
def part2(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
        total = 0
        for line in lines:
            _, attempts = line.split(': ')
            total += get_power(attempts)
    return total


if __name__ == '__main__':
    assert part1('test.txt') == 8
    print(part1('input.txt'))
    assert part2('test.txt') == 2286
    print(part2('input.txt'))
