from itertools import combinations
from typing import List
from common.utils import read_file
import networkx as nx
from multiprocessing import Pool

def calculate_distance(args):
    graph, uv = args
    u, v = uv
    return nx.shortest_path_length(graph, u, v)

def p1(input_data: List[str]):
    grid = [list(line) for line in input_data]
    # if there is a row with only dots, insert a row of dots above it
    new_grid = []
    for line in grid:
        new_grid.append(line)
        if all([tile == "." for tile in line]):
            new_grid.append(["." for tile in line])

    # do the same for columns
    transposed_grid = list(zip(*new_grid))
    new_grid_2 = []
    for line in transposed_grid:
        if all([tile == "." for tile in line]):
            new_grid_2.append(["." for tile in line])
        new_grid_2.append(line)

    # transpose back
    grid = list(zip(*new_grid_2))

    graph = nx.Graph()
    galaxies = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            tile = grid[y][x]

            current_node = (y, x)

            if tile == "#":
                galaxies.append(current_node)

            north = (y-1, x)
            south = (y+1, x)
            east = (y, x+1)
            west = (y, x-1)

            # add edge to each direction
            graph.add_edge(current_node, north)
            graph.add_edge(current_node, south)
            graph.add_edge(current_node, east)
            graph.add_edge(current_node, west)

    # Use multiprocessing to parallelize the calculation
    with Pool() as pool:
        args_list = [(graph, uv) for uv in combinations(galaxies, 2)]
        total_distance = sum(pool.map(calculate_distance, args_list))

    return total_distance

def p2(input_data: List[str]):
    grid = [list(line) for line in input_data]
    # if there is a row with only dots, insert a row of dots above it
    new_grid = []
    for line in grid:
        new_grid.append(line)

    # do the same for columns
    transposed_grid = list(zip(*new_grid))
    new_grid_2 = []
    for line in transposed_grid:
        new_grid_2.append(line)

    # transpose back
    grid = list(zip(*new_grid_2))

    graph = nx.Graph()
    galaxies = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            tile = grid[y][x]

            current_node = (y, x)

            if tile == "#":
                galaxies.append(current_node)

            north = (y-1, x)
            south = (y+1, x)
            east = (y, x+1)
            west = (y, x-1)

            # add edge to each direction
            graph.add_edge(current_node, north)
            graph.add_edge(current_node, south)
            graph.add_edge(current_node, east)
            graph.add_edge(current_node, west)

    # Use multiprocessing to parallelize the calculation
    with Pool() as pool:
        args_list = [(graph, uv) for uv in combinations(galaxies, 2)]
        total_distance = sum(pool.map(calculate_distance, args_list))

    return total_distance

if __name__ == "__main__":
    input_data = read_file("11/input.txt")
    # result = p2(input_data)

    zero = 9609066
    one = 15208074
    diff = (one - zero) * 1000000
    next_number = one + (diff * 10)
    print(next_number)


    # print(result)


