with open('3.txt', 'r') as f:
    intersections = []
    for line in f.readlines():
        line = line.strip()
        len_ = len(line)
        str1, str2 = line[:len_ // 2], line[len_ // 2:]
        intersections += list(set(str1).intersection(str2))
# Lowercase item types a through z have priorities 1 through 26. 97-122 -96
# Uppercase item types A through Z have priorities 27 through 52. 65-90  -38
sum_intersections = sum((ord(i) - 96) if i.islower() else (ord(i) - 38) for i in intersections)
print(sum_intersections)


with open('3.txt', 'r') as f:
    lines = [line.split() for line in f.readlines()]
    intersections = []
    for i in range(2, len(lines), 3):
        first, second, third = lines[i-2][0], lines[i-1][0], lines[i][0]
        intersections += list(set(first).intersection(set(second)).intersection(set(third)))
sum_intersections = sum((ord(i) - 96) if i.islower() else (ord(i) - 38) for i in intersections)
print(sum_intersections)
