import re

with open('input.txt', 'r') as f:
    counter = 0
    counter2 = 0
    for line in f.readlines():
        f_start, f_end, s_start, s_end = [int(num) for num in re.split('[,-]', line)]
        first_set = set([i for i in range(f_start, f_end + 1)])
        second_set = set([i for i in range(s_start, s_end + 1)])
        overlap = first_set & second_set
        # if first_set.issubset(second_set) or second_set.issubset(first_set):
        if len(overlap) in (len(first_set), len(second_set)):
            counter += 1
        if len(overlap) != 0:
            counter2 += 1

print(counter)
print(counter2)
