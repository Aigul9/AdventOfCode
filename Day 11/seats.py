from copy import deepcopy


def seats_sum(arr):
    return sum(row.count('#') for row in arr)


def get_adjacent_seats_part1(i, j, arr):
    adj_count = 0
    for d_i, d_j in directions:
        if 0 <= i + d_i < len(arr) and 0 <= j + d_j < len(arr[0]) and arr[i + d_i][j + d_j] == '#':
            adj_count += 1
    return adj_count


def get_adjacent_seats_part2(i, j, arr):
    adj_count = 0
    for d_i, d_j in directions:
        r = i + d_i
        c = j + d_j
        while 0 <= r < rows and 0 <= c < cols:
            if arr[r][c] != '.':
                adj_count += 1 if arr[r][c] == '#' else 0
                break
            r += d_i
            c += d_j
    return adj_count


def change_state(arr, num, func):
    seats_copy = deepcopy(arr)
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 'L' and eval(func)(i, j, arr) == 0:
                seats_copy[i][j] = '#'
            elif arr[i][j] == '#' and eval(func)(i, j, arr) >= num:
                seats_copy[i][j] = 'L'
    return seats_copy


def start(arr, num, func):
    prev_arr = None
    while prev_arr != arr:
        prev_arr = arr
        arr = change_state(arr, num, func)
    return seats_sum(arr)


with open('seats.txt', 'r') as f:
    seats = [list(line.strip()) for line in f.readlines()]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
rows = len(seats)
cols = len(seats[0])
# part 1
print(start(seats, 4, 'get_adjacent_seats_part1'))
# part 2
print(start(seats, 5, 'get_adjacent_seats_part2'))
