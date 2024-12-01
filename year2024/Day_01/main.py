from collections import Counter

from utils.measure import timeit, memory


def read(path):
    with open(path, 'r') as f:
        left = []
        right = []

        for line in f:
            num_left, num_right = list(map(int, line.split()))
            left.append(num_left)
            right.append(num_right)

    return left, right


@timeit
@memory
def part1(left, right):
    total = sum(abs(num_left - num_right) for num_left, num_right in zip(sorted(left), sorted(right)))
    return total


@timeit
@memory
def part2(left, right):
    right_counter = Counter(right)
    total = sum(left_num * right_counter.get(left_num, 0) for left_num in left)
    return total


if __name__ == '__main__':
    # read
    test_left, test_right = read('test.txt')
    input_left, input_right = read('input.txt')

    # part1
    print(part1(test_left, test_right))
    assert part1(test_left, test_right) == 11

    print(part1(input_left, input_right))

    # part2
    print(part2(test_left, test_right))
    assert part2(test_left, test_right) == 31

    print(part2(input_left, input_right))


