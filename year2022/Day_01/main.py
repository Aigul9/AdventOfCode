def max_calories(path, n):
    with open(path, 'r') as f:
        calories = f.read().split('\n\n')
        calories = [sum(map(int, line.split())) for line in calories]
        return sum(sorted(calories)[-n:])


assert max_calories('test.txt', 1) == 24000
print(max_calories('input.txt', 1))
assert max_calories('test.txt', 3) == 45000
print(max_calories('input.txt', 3))
