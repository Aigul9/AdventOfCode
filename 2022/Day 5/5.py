import copy
import re
from collections import defaultdict

transition = {0: 1, 4: 2, 8: 3}


def find_all(s, c):
    idx = s.find(c)
    while idx != -1:
        yield idx
        idx = s.find(c, idx + 1)


with open('5.txt', 'r') as f:
    stacks = defaultdict(list, {k: [] for k in (1, 2, 3)})
    instructions = []
    for line in f.readlines():
        idx_gen = find_all(line, '[')
        for i in idx_gen:
            stacks[i // 4 + 1].append(line[i + 1])
        if 'move' in line:
            instructions.append([int(i) for i in list(filter(None, re.split(r'[a-z\s]+', line.strip())))])


stacks = {k: list(reversed(v)) for k, v in sorted(stacks.items(), key=lambda k: k[0])}
stacks2 = copy.deepcopy(stacks)
for i in instructions:
    move, from_, to = i
    stacks[to] += reversed(stacks[from_][-move:])
    stacks2[to] += stacks2[from_][-move:]
    del stacks[from_][-move:]
    del stacks2[from_][-move:]
res = ''.join([v[-1] for k, v in stacks.items()])
res2 = ''.join([v[-1] for k, v in stacks2.items()])
print(res, res2)
