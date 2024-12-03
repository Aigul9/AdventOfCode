import re

from utils.measure import timeit, memory


def read(path):
    with open(path, 'r') as f:
        text = f.read()
    return text


@timeit
@memory
def part1(data):
    total = 0
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    matches = re.findall(pattern, data)

    for match in matches:
        num1, num2 = list(map(int, re.findall('\\d+', match)))
        total += num1 * num2

    return total


def part2(data):
    total = 0
    pattern = r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)'
    matches = re.findall(pattern, data)
    is_enabled = True
    enabled_dict = {
        'do()': True,
        "don't()": False
    }

    for match in matches:
        if 'do' in match:
            is_enabled = enabled_dict[match]
            continue

        if is_enabled:
            num1, num2 = list(map(int, re.findall('\\d+', match)))
            total += num1 * num2
            continue

    return total


if __name__ == '__main__':
    # read
    test_data = read('test.txt')
    input_data = read('input.txt')
    test_data2 = read('test2.txt')

    # part1
    print(part1(test_data))
    assert part1(test_data) == 161

    print(part1(input_data))

    # part2
    print(part2(test_data2))
    assert part2(test_data2) == 48

    print(part2(input_data))
