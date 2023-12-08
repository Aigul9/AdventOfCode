import itertools
import re


class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right


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
    current_list = [node for node in nodes if node.name.endswith(start_letter)]
    print(current_list)
    num_steps = 0

    # for i in itertools.cycle(instruction):
    #     if len([node for node in current_list if node.name.endswith(end_letter)]) == len(current_list):
    #         break
    #
    #     if i == 'L':
    #         current_list = [node for node in nodes for current_node in current_list if node.name == current_node.left]
    #     elif i == 'R':
    #         current_list = [node for node in nodes for current_node in current_list if node.name == current_node.right]
    #     num_steps += 1
        # print(i, [node.name for node in current_list])

    print(current_list)
    print(num_steps)
    return num_steps


if __name__ == '__main__':
    # print(part1(read_file('test.txt')))
    # print(part1(read_file('test2.txt')))
    # print(part1(read_file('input.txt')))

    print(part2(read_file('test3.txt')))
    # print(part2(read_file('input.txt')))
