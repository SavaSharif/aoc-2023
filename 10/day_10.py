from typing import List, Dict, Tuple

from common.utils import read_file
import networkx as nx

def p1(input_data: List[str]):
    grid = [list(line) for line in input_data]

    graph = nx.DiGraph()
    start_node = None

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            tile = grid[y][x]

            if tile == ".":
                continue

            current_node = (y, x)
            north = (y-1, x)
            south = (y+1, x)
            east = (y, x+1)
            west = (y, x-1)

            if tile == "S":
                start_node = current_node
                graph.add_edge(current_node, north)
                graph.add_edge(current_node, south)
                graph.add_edge(current_node, east)
                graph.add_edge(current_node, west)

            elif tile == "L":
                graph.add_edge(current_node, north)
                graph.add_edge(current_node, east)

            elif tile == "J":
                graph.add_edge(current_node, north)
                graph.add_edge(current_node, west)

            elif tile == "7":
                graph.add_edge(current_node, south)
                graph.add_edge(current_node, west)

            elif tile == "F":
                graph.add_edge(current_node, south)
                graph.add_edge(current_node, east)

            elif tile == "|":
                graph.add_edge(current_node, north)
                graph.add_edge(current_node, south)

            elif tile == "-":
                graph.add_edge(current_node, west)
                graph.add_edge(current_node, east)

            
    graph = graph.to_undirected(reciprocal=True)

    longest_distance = nx.single_source_dijkstra_path_length(graph, source=start_node).values()

    return max(longest_distance)

def p2(input_data: List[str]):
    grid = [list(line) for line in input_data]

    graph = nx.DiGraph()
    start_node = None

    dimensions = (len(grid), len(grid[0]))

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            tile = grid[y][x]



            current_node = (y, x)
            north = (y-1, x)
            south = (y+1, x)
            east = (y, x+1)
            west = (y, x-1)

            if tile == ".":
                graph.add_node(current_node)
                # only add edges to its neighbours if they are also .
                if north[0] >= 0 and grid[north[0]][north[1]] == ".":
                    graph.add_edge(current_node, north)
                if south[0] < dimensions[0] and grid[south[0]][south[1]] == ".":
                    graph.add_edge(current_node, south)
                if east[1] < dimensions[1] and grid[east[0]][east[1]] == ".":
                    graph.add_edge(current_node, east)
                if west[1] >= 0 and grid[west[0]][west[1]] == ".":
                    graph.add_edge(current_node, west)

            if tile == "S":
                start_node = current_node
                graph.add_edge(current_node, north)
                graph.add_edge(current_node, south)
                graph.add_edge(current_node, east)
                graph.add_edge(current_node, west)

            elif tile == "L":
                graph.add_edge(current_node, north)
                graph.add_edge(current_node, east)

            elif tile == "J":
                graph.add_edge(current_node, north)
                graph.add_edge(current_node, west)

            elif tile == "7":
                graph.add_edge(current_node, south)
                graph.add_edge(current_node, west)

            elif tile == "F":
                graph.add_edge(current_node, south)
                graph.add_edge(current_node, east)

            elif tile == "|": # vertical pipe
                graph.add_edge(current_node, north)
                graph.add_edge(current_node, south)

            elif tile == "-": # horizontal pipe
                graph.add_edge(current_node, west)
                graph.add_edge(current_node, east)

            
    graph = graph.to_undirected(reciprocal=True)

    # get all connected components
    connected_components = nx.connected_components(graph)

    # main component is the one that contains the start node
    main_component = None
    connected_components = list(connected_components)
    for component in connected_components:
        if start_node in component:
            main_component = component
            break

    # for each connected component, check the surrounding nodes of that component in the grid
    # if there is a 7,f,j or l, remove that component
    for component in connected_components:
        if component == main_component:
            continue

        for node in component:
            y, x = node
            surrounding_nodes = [
                (y-1, x),
                (y+1, x),
                (y, x-1),
                (y, x+1)
            ]
            # check that there are no consequtive non pipe tiles
            for node in surrounding_nodes:
                y, x = node
                if y < 0 or y >= dimensions[0] or x < 0 or x >= dimensions[1]:
                    continue
                tile = grid[y][x]
                if tile in ["7", "F", "J", "L"]:
                    connected_components.remove(component)
                    break
        print(component)

    
        
        
    # remove main component from connected components
    connected_components.remove(main_component)
    print(connected_components)


if __name__ == "__main__":
    input_data = read_file("10/input.txt")
    # result = p1(input_data)
    result = p2(input_data)
    print(result)

