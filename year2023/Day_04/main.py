import re

from utils.measure import timeit, memory


def get_num_set(input_list):
    return set(map(int, input_list.split()))


def sum_values(n):
    return 2 ** (n - 1) if n > 0 else 0


@timeit
@memory
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


@timeit
@memory
def part2(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
        copies_dict = {}
        max_card_num = len(lines)
        for line in lines:
            card_num, win_list, my_list = re.split(r': | \| ', line)
            _, card_num = card_num.split()
            card_num = int(card_num)
            win_list = get_num_set(win_list)
            my_list = get_num_set(my_list)
            copies_num = len(win_list & my_list)
            for i in range(card_num + 1, card_num + copies_num + 1):
                copies_dict[i] = copies_dict.get(i, 0) + 1 + copies_dict.get(card_num, 0)

    return sum(v for v in copies_dict.values()) + max_card_num


if __name__ == '__main__':
    assert part1('test.txt') == 13
    print(part1('input.txt'))
    assert part2('test.txt') == 30
    print(part2('input.txt'))
