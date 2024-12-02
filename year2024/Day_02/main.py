from utils.measure import timeit, memory


def read(path):
    with open(path, 'r') as f:
        return [list(map(int, line.strip().split())) for line in f.readlines()]


@timeit
@memory
def part1(data):
    total = 0

    for row in data:
        if is_safe(row):
            total += 1

    return total


def is_safe(row):
    row_diff = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    min_num, max_num = min(row_diff), max(row_diff)

    return -3 <= min_num <= max_num <= -1 or 1 <= min_num <= max_num <= 3


@timeit
@memory
def part2(data):
    total = 0

    for row in data:
        for idx in range(len(row)):
            row_copy = row[:idx] + row[idx+1:]
            if is_safe(row_copy):
                total += 1
                break

    return total


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
