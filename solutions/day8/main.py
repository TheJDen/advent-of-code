from collections import namedtuple
from itertools import cycle

Node = namedtuple("Node", ["left", "right"])

def part1(instructions, nodes_by_name, start_name="AAA", end_condition = lambda node_name: node_name == "ZZZ"):
    node_name = start_name
    for num_steps, instruction in enumerate(cycle(instructions), start=1):
        node_name = nodes_by_name[node_name].left if instruction == 'L' else nodes_by_name[node_name].right
        if end_condition(node_name):
            return num_steps
        
import math   
def part2(instructions, nodes_by_name):
    steps_to_z = [part1(instructions, nodes_by_name, node_name, lambda name: name.endswith('Z')) for node_name in nodes_by_name if node_name.endswith('A')]
    return math.lcm(*steps_to_z)

def parse_input(lines):
    instructions = next(lines)
    next(lines)
    nodes_by_name = {}
    for line in lines:
        name, neighbors = line.split(" = ")
        left, right = neighbors.strip("()").split(', ')
        nodes_by_name[name] = Node(left, right)
    return instructions, nodes_by_name

def main():
    with open("input.txt") as f:
        instructions, nodes_by_name = parse_input((line.rstrip() for line in f))
    print(part1(instructions, nodes_by_name))
    print(part2(instructions, nodes_by_name))


if __name__ == "__main__":
    main()