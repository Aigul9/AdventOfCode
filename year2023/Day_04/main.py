import re

from utils.measure import timeit, memory


def get_num_set(input_list):
    return set(map(int, input_list.split()))


def sum_values(n):
    return 2 ** (n - 1) if n > 0 else 0


def part1(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
        total = 0
        for line in lines:
            _, win_list, my_list = re.split(r': | \| ', line)
            win_list = get_num_set(win_list)
            my_list = get_num_set(my_list)
            total += sum_values(len(win_list & my_list))
        return total


if __name__ == '__main__':
    assert part1('test.txt') == 13
    print(part1('input.txt'))
    # assert part2('test.txt') == 467835
    # print(part2('input.txt'))
