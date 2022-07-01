with open("input.txt", "r") as f:
    instructions = [line.rstrip('\n').split() for line in f]


def part1(x, y):
    for row in instructions:
        direction, value = row[0], int(row[1])
        if direction == 'forward':
            x += value
        elif direction == 'down':
            y += value
        elif direction == 'up':
            y -= value
    return x * y


def part2(x, y, aim):
    for row in instructions:
        direction, value = row[0], int(row[1])
        if direction == 'forward':
            x += value
            y += aim * value
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
    return x * y


print(part1(0, 0))
print(part2(0, 0, 0))
