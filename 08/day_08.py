from math import gcd
import networkx as nx
import re
from typing import List
import matplotlib.pyplot as plt
from common.utils import read_file
import random


class TreeNode:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None



def p1(input: List[str]) -> int:
    instructions = list(input.pop(0))
    input.pop(0)

    regex = r"(\w+) = \((\w+), (\w+)\)"
    nodes = {}

    root = None
    dest = None
    for line in input:
        parent, child_l, child_r = re.match(regex, line).groups()

        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if child_l not in nodes:
            nodes[child_l] = TreeNode(child_l)
        if child_r not in nodes:
            nodes[child_r] = TreeNode(child_r)

        nodes[parent].left = nodes[child_l]
        nodes[parent].right = nodes[child_r]

    root = "AAA"
    dest = "ZZZ"
    step_count = 0
    current_node = nodes[root]
    while current_node.label != dest:
        for instruction in instructions:
            current_node = current_node.left if instruction == "L" else current_node.right
            step_count += 1
            
    return step_count

def p2(input: List[str]) -> int:
    instructions = list(input.pop(0))
    input.pop(0)

    regex = r"(\w+) = \((\w+), (\w+)\)"
    nodes = {}

    for line in input:
        parent, child_l, child_r = re.match(regex, line).groups()

        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if child_l not in nodes:
            nodes[child_l] = TreeNode(child_l)
        if child_r not in nodes:
            nodes[child_r] = TreeNode(child_r)

        nodes[parent].left = nodes[child_l]
        nodes[parent].right = nodes[child_r]

    starting_nodes = [node for node in nodes if node.endswith("A")]
    # starting_nodes = [starting_nodes[5]]
    print("Created starting nodes: ", starting_nodes)
    
    # # now simultaneously walk the tree from all starting nodes. End when each starting node has reached its destination
    # step_count = 0
    # # keep going while t
    # while not all([node.endswith("Z") for node in starting_nodes]):
    # step_count = 0
    # for instruction in instructions:
    #     for i, node in enumerate(starting_nodes):
    #         if instruction == "L":
    #             starting_nodes[i] = nodes[node].left.label
    #             step_count += 1
    #         elif instruction == "R":
    #             starting_nodes[i] = nodes[node].right.label
    #             step_count += 1
    # print(step_count)

    # root = "AAA"
    # dest = "ZZZ"
    step_counts = []
    for node in starting_nodes:
        step_count = 0
        current_node = nodes[node]
        while not current_node.label.endswith("Z"):
            for instruction in instructions:
                current_node = current_node.left if instruction == "L" else current_node.right
                step_count += 1
        step_counts.append(step_count)

    print(step_counts)

    lcm = step_counts[0]
    for i in step_counts[1:]:
        lcm = lcm * i // gcd(lcm, i)
    print(lcm)

    

if __name__ == "__main__":
    # 14893 * 19951 * 22199 * 16579 * 17141 * 12083
    # print(14893 * 19951 * 22199 * 16579 * 17141 * 12083)
    input_data = read_file("08/input.txt")
    # result = p1(input_data)
    result = p2(input_data)

    # print(result)
