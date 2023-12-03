import re

from utils.measure import timeit, memory


directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]


def is_adjacent(grid, i, j):
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and re.search(r'[^0-9.]', grid[ni][nj]) is not None:
            return True
    return False


@timeit
@memory
def part1(path):
    with open(path, 'r') as f:
        grid = f.read().split('\n')
        total = 0
        for row_idx in range(len(grid)):
            row = grid[row_idx]
            numbers = [(int(m.group()), m.start(), m.end()) for m in re.finditer(r'\d+', row)]
            for num, i_start, i_end in numbers:
                for num_idx in range(i_start, i_end):
                    if is_adjacent(grid, row_idx, num_idx):
                        total += num
                        break
    return total


def is_asterisk_found(grid, i, j):
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '*':
            return ni, nj
    return False


@timeit
@memory
def part2(path):
    with open(path, 'r') as f:
        grid = f.read().split('\n')

        asterisk_dict = {}

        for row_idx in range(len(grid)):
            row = grid[row_idx]
            numbers = [(int(m.group()), m.start(), m.end()) for m in re.finditer(r'\d+', row)]
            for num, i_start, i_end in numbers:
                for num_idx in range(i_start, i_end):
                    asterisk_coord = is_asterisk_found(grid, row_idx, num_idx)

                    if not asterisk_coord:
                        continue

                    if asterisk_coord not in asterisk_dict:
                        asterisk_dict[asterisk_coord] = {'occurrences': 1, 'ratio': num}
                    else:
                        asterisk_dict[asterisk_coord]['occurrences'] += 1
                        asterisk_dict[asterisk_coord]['ratio'] *= num
                    break

    return sum(v['ratio'] for v in asterisk_dict.values() if v['occurrences'] == 2)


if __name__ == '__main__':
    assert part1('test.txt') == 4361
    print(part1('input.txt'))
    assert part2('test.txt') == 467835
    print(part2('input.txt'))
