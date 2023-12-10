import numpy as np

pipes = {
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((0, -1), (-1, 0)),
    '7': ((0, -1), (1, 0)),
    'F': ((0, 1), (1, 0)),
}

# pipes_reversed = {
#     (0, 1): ['-', 'L', 'F'],
#     (1, 0): ['|', '7', 'F'],
#     (0, -1): ['-', 'J', '7'],
#     (-1, 0): ['|', 'L', 'J']
# }

sides = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def process(pipe, current_indices, next_indices):
    pipe_first, pipe_second = pipes[pipe]
    left = (next_indices[0] + pipe_first[0], next_indices[1] + pipe_first[1])
    right = (next_indices[0] + pipe_second[0], next_indices[1] + pipe_second[1])
    if left == current_indices:
        return next_indices, right
    elif right == current_indices:
        return next_indices, left
    else:
        return None


def part1(path):
    with open(path, 'r') as f:
        sketch = np.array([list(line) for line in f.read().split('\n')])
        indices = np.where(sketch == 'S')
        current_indices = indices[0][0], indices[1][0]
        total = 2

        for side in sides:
            side_idx = current_indices[0] + side[0], current_indices[1] + side[1]
            pipe = sketch[side_idx]
            res = process(pipe, current_indices, side_idx)
            if res is not None:
                current_indices, next_indices = res
                break

        while True:
            pipe = sketch[next_indices]

            if pipe == 'S' and total > 0:
                break

            current_indices, next_indices = process(pipe, current_indices, next_indices)
            total += 1

        return int(total / 2)


if __name__ == '__main__':
    print(part1('test.txt'))
    print(part1('test2.txt'))
    print(part1('test3.txt'))
    print(part1('input.txt'))
