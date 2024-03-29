from utils.measure import timeit

digit_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


@timeit
def part1():
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n')
        total = 0
        for line in lines:
            digits = ''.join([char for char in line if char.isdigit()])
            total += int(digits[0] + digits[-1])
        print(total)


def get_substring(input_line, is_end=False):
    new_line_part = ''

    for char in input_line:
        new_line_part = new_line_part + char if not is_end else char + new_line_part

        for k, v in digit_dict.items():
            if k in new_line_part:
                new_line_part = new_line_part.replace(k, v)
                return new_line_part

    return new_line_part


@timeit
def part2():
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n')
        total = 0

        for line in lines:
            new_line_start = get_substring(line)
            new_line_end = get_substring(line[::-1], True)
            new_line = new_line_start + new_line_end
            digits = ''.join([char for char in new_line if char.isdigit()])
            total += int(digits[0] + digits[-1])
        print(total)


if __name__ == '__main__':
    part1()
    part2()
