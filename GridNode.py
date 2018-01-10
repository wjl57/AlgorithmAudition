import math


class GridNode:
    def __init__(self, node_type, x, y):
        self.node_type = node_type
        self.x = x
        self.y = y
        # Map from neighboring nodes to the cost to reach that node from the current node
        self.neighbors = {}

    def coordinate_string(self):
        return "(" + str(self.x).rjust(2) + "," + str(self.y).rjust(2) + ")"

    def __str__(self):
        num_neighbor_string = "(" + str(len(self.neighbors)) + " neighbors)"
        neighbor_strings = [neighbor.coordinate_string() for neighbor in self.neighbors]
        neighbors_string = ", ".join(neighbor_strings)
        return self.coordinate_string() + " " + num_neighbor_string + ": " + neighbors_string

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.y < other.y if self.x == other.x else self.x < other.x

    def __hash__(self):
        return hash(str(self.x) + " " + str(self.y))

    @staticmethod
    def manhattan_distance(node1, node2):
        return abs(node1.x - node2.x) + abs(node1.y - node2.y)

    @staticmethod
    def euclidean_distance(node1, node2):
        return math.sqrt(math.pow(node1.x - node2.x, 2) + math.pow((node1.y - node2.y), 2))

