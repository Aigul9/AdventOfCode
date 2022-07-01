import re
from math import prod


def chinese_remainder_theorem(bus, ofs):
    p = prod(bus)
    res = sum(b * (p // o) * pow(p // o, -1, o) for o, b in zip(bus, ofs))
    return res % p


with open('bus.txt', 'r') as f:
    stamp = int(f.readline().rstrip())
    line = f.readline().rstrip()
    buses = list(map(int, re.findall(r'(\d+)', line)))
    offset = [(int(b) - i) for i, b in enumerate(line.split(',')) if b != 'x']

diff = [b - stamp % b for b in buses]
print(min(diff) * buses[diff.index(min(diff))])
print(chinese_remainder_theorem(buses, offset))
