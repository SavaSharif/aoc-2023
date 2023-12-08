import networkx as nx
import re
from typing import List
import matplotlib.pyplot as plt
from common.utils import read_file
import random

def p1(input: List[str]) -> int:
    instructions = list(input.pop(0))
    input.pop(0)

    regex = r"(\w+) = \((\w+), (\w+)\)"
 
    root = None
    destination = None
    G = nx.Graph()
    for i, line in enumerate(input):

        parent, child_l, child_r = re.findall(regex, line)[0]
        if i == 0:
            root = parent

        if i == int(len(input) -1 ):
            destination = parent

        G.add_edge(parent, child_l, weight=0)
        G.add_edge(parent, child_r, weight=1)

     # Plotting the network
    pos = nx.spring_layout(G, seed=42)
    labels = {node: node for node in G.nodes()}

    nx.draw(G, with_labels=True, labels=labels, node_size=700, node_color='skyblue', font_size=8)

    plt.title("Network Visualization")
    plt.show()

    # tree = nx.bfs_tree(G, root)
    
    # plo

    # # traverse the tree based on the instructions
    # step_count = 0
    # current_node = root
    # # while current_node != destination:
    # for instruction in instructions:
    #     # check if we have any children
    #     if len(list(tree.neighbors(current_node))) == 0:
    #         break
    #     # get edges of the current node with labels
    #     edges = list(G.edges(current_node, data=True))
    #     if instruction == "L":
    #         current_node = edges[0][1]
    #     else:
    #         current_node = edges[1][1]

            

        
    
    # return step_count


def plot_tree(G, root=None):
    pos = hierarchy_pos(G, root)
    # edge_labels = nx.get_edge_attributes(G, 'label')
    labels = {node: node for node in G.nodes()}

    nx.draw(G, pos, with_labels=True, labels=labels, node_size=700, node_color='skyblue', font_size=8)
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)

    plt.title("Network Visualization")
    plt.show()
    
def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''
    
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos

            
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

if __name__ == "__main__":
    input_data = read_file("08/input.txt")
    result = p1(input_data)
    # result = p2(input_data)

    print(result)
