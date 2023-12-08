import itertools
import math
import re

from AdventOfCode.utils.measure import timeit, memory


def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
        instruction, network = lines[0], lines[2:]
        nodes = {}
        for line in network:
            node, left, right = re.findall(r'\w+', line)
            nodes[node] = (left, right)
        return instruction, nodes


@timeit
@memory
def part1(data):
    instruction, nodes = data
    current, end = 'AAA', 'ZZZ'
    num_steps = 0
    for i in itertools.cycle(instruction):
        if current == end:
            break

        if i == 'L':
            current = nodes[current][0]
        elif i == 'R':
            current = nodes[current][1]
        num_steps += 1

    return num_steps


@timeit
@memory
def part2(data):
    instruction, nodes = data
    start_letter, end_letter = 'A', 'Z'
    starting_list = [k for k, v in nodes.items() if k.endswith(start_letter)]
    num_steps_set = set()

    for start_node in starting_list:
        current = start_node
        num_steps = 0
        for i in itertools.cycle(instruction):
            if current.endswith(end_letter):
                num_steps_set.add(num_steps)
                break

            if i == 'L':
                current = nodes[current][0]
            elif i == 'R':
                current = nodes[current][1]
            num_steps += 1

    return math.lcm(*num_steps_set)


if __name__ == '__main__':
    print(part1(read_file('test.txt')))
    print(part1(read_file('test2.txt')))
    print(part1(read_file('input.txt')))

    print(part2(read_file('test3.txt')))
    print(part2(read_file('input.txt')))
