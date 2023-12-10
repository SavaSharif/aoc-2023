import re
from typing import List

from matplotlib import pyplot as plt
from common.utils import read_file
import networkx as nx


def p1(input: List[str]) -> int:
    G = {}  # Use a dictionary to represent the graph

    grid = []

    for i, line in enumerate(input):
        tiles = list(line)
        grid.append(tiles)

    for y in range(len(grid)):
        for x in range(len(grid[i])):
            tile = grid[y][x]

            if tile == ".":
                continue

            current_node = (y, x)

            if tile in {"|", "-", "L", "J", "7", "F", "S"}:
                G[current_node] = []

            if tile == "L":
                G[current_node].append((y, x+1))
                G[current_node].append((y-1, x))

            elif tile == "J":
                G[current_node].append((y, x-1))
                G[current_node].append((y-1, x))

            elif tile == "7":
                G[current_node].append((y, x-1))
                G[current_node].append((y+1, x))

            elif tile == "F":
                G[current_node].append((y, x+1))
                G[current_node].append((y+1, x))

            elif tile == "|":
                G[current_node].append((y-1, x))
                G[current_node].append((y+1, x))

            elif tile == "-":
                G[current_node].append((y, x-1))
                G[current_node].append((y, x+1))

            elif tile == "S":
                G[current_node] = []



if __name__ == "__main__":
    input_data = read_file("10/input.txt")
    result = p1(input_data)
    # result = p2(input_data)
    print(result)
