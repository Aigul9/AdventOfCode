from utils.measure import timeit, memory


def read(path):
    with open(path, 'r') as f:
        return [list(map(int, line.strip().split())) for line in f.readlines()]


def is_safe(row):
    row_diff = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    min_num, max_num = min(row_diff), max(row_diff)

    return -3 <= min_num <= max_num <= -1 or 1 <= min_num <= max_num <= 3


@timeit
@memory
def part1(data):
    return sum(is_safe(row) for row in data)


@timeit
@memory
def part2(data):
    return sum(any(is_safe(row[:idx] + row[idx + 1:]) for idx in range(len(row))) for row in data)


if __name__ == '__main__':
    # read
    test_data = read('test.txt')
    input_data = read('input.txt')

    # part1
    print(part1(test_data))
    assert part1(test_data) == 2

    print(part1(input_data))

    # part2
    print(part2(test_data))
    assert part2(test_data) == 4

    print(part2(input_data))
