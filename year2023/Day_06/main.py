import math
from functools import reduce

from utils.measure import timeit, memory


def get_num_ways(time, dst):
    sqrt_discriminant = (time ** 2 - 4 * dst) ** 0.5
    x1 = (time - sqrt_discriminant) / 2
    x2 = (time + sqrt_discriminant) / 2
    start = math.ceil(x1) if not x1.is_integer() else int(x1 + 1)
    end = math.floor(x2) if not x2.is_integer() else int(x2 - 1)
    return len(range(start, end + 1))


@timeit
@memory
def part1(path):
    with open(path, 'r') as f:
        time_list, dst_list = (list(map(int, line.split()[1:])) for line in f.read().split('\n'))
        return reduce(lambda x, y: x * y, [get_num_ways(time, dst) for time, dst in zip(time_list, dst_list)])


@timeit
@memory
def part2(path):
    with open(path, 'r') as f:
        time_num, dst_num = (int(line.split(':')[1:][0].replace(' ', '')) for line in f.read().split('\n'))
        return get_num_ways(time_num, dst_num)


if __name__ == '__main__':
    assert part1('test.txt') == 288
    print(part1('input.txt'))
    assert part2('test.txt') == 71503
    print(part2('input.txt'))
