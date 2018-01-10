import os
from collections import defaultdict
from itertools import combinations

import math

from GridNode import GridNode
from NodeTypes import NodeTypes


class GridReader:
    def __init__(self):
        self.source_node = None
        self.destination_node = None
        self.grid_nodes = []
        self.node_type_map = {
            '.': NodeTypes.NORMAL,
            'W': NodeTypes.WALL,
            'S': NodeTypes.SOURCE,
            'D': NodeTypes.DESTINATION
        }

    def read_terrain(self, relative_file_path):
        absolute_file_path = os.path.join(os.path.dirname(__file__), relative_file_path)
        file = open(absolute_file_path)

        y = 0
        for line in file:
            x = 0
            for c in line.rstrip():
                node_type = self.node_type_map[c]
                node = GridNode(node_type, x, y)
                self.grid_nodes.append(node)
                if node_type == NodeTypes.SOURCE:
                    self.source_node = node
                elif node_type == NodeTypes.DESTINATION:
                    self.destination_node = node

                x += 1
            y += 1

    def add_lateral_neighbors(self):
        for (node1, node2) in combinations(self.grid_nodes, 2):
            if node1.node_type == NodeTypes.WALL or node2.node_type == NodeTypes.WALL:
                continue
            x_delta = abs(node1.x - node2.x)
            y_delta = abs(node1.y - node2.y)
            if (x_delta == 1 and y_delta == 0) or (x_delta == 0 and y_delta == 1):
                # Distance of 1
                node1.neighbors[node2] = 1
                node2.neighbors[node1] = 1

    def add_diagonal_neighbors(self):
        for (node1, node2) in combinations(self.grid_nodes, 2):
            if node1.node_type == NodeTypes.WALL or node2.node_type == NodeTypes.WALL:
                continue
            x_delta = abs(node1.x - node2.x)
            y_delta = abs(node1.y - node2.y)
            if x_delta == 1 and y_delta == 1:
                # Distance of sqrt(2)
                node1.neighbors[node2] = math.sqrt(2)
                node2.neighbors[node1] = math.sqrt(2)
