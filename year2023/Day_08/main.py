import itertools
import math
import re


class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right


def find_gcd(input_set):
    x = reduce(gcd, input_set)
    return x


def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
        instruction, network = lines[0], lines[2:]
        nodes = []
        for line in network:
            node, left, right = re.findall(r'\w+', line)
            nodes.append(Node(node, left, right))
        return instruction, nodes


def part1(data):
    instruction, nodes = data
    current, end = 'AAA', 'ZZZ'
    num_steps = 0
    for i in itertools.cycle(instruction):
        if current == end:
            break

        if i == 'L':
            current = [node.left for node in nodes if node.name == current][0]
        elif i == 'R':
            current = [node.right for node in nodes if node.name == current][0]
        num_steps += 1

    return num_steps


def part2(data):
    instruction, nodes = data
    start_letter, end_letter = 'A', 'Z'
    starting_list = [node for node in nodes if node.name.endswith(start_letter)]
    num_steps_set = set()

    for start_node in starting_list:
        current_node_name = start_node.name
        num_steps = 0
        for i in itertools.cycle(instruction):
            if current_node_name.endswith(end_letter):
                num_steps_set.add(num_steps)
                break

            if i == 'L':
                current_node_name = [node.left for node in nodes if node.name == current_node_name][0]
            elif i == 'R':
                current_node_name = [node.right for node in nodes if node.name == current_node_name][0]
            num_steps += 1

    return math.lcm(*num_steps_set)


if __name__ == '__main__':
    print(part1(read_file('test.txt')))
    print(part1(read_file('test2.txt')))
    print(part1(read_file('input.txt')))

    print(part2(read_file('test3.txt')))
    print(part2(read_file('input.txt')))
