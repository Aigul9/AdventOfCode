import re


p = re.compile(r'^(\d+)-(\d+) (.): (.*)$')

with open('passwords.txt', 'r') as f:
    valid_count = valid_index = 0

    for line in f:
        (first, second, letter, pw) = p.match(line.strip()).groups()
        first, second = int(first), int(second)

        if first <= pw.count(letter) <= second:
            valid_count += 1
        if (pw[first - 1] == letter) ^ (pw[second - 1] == letter):
            valid_index += 1

print(valid_count, valid_index)
