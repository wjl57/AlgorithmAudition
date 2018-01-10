import sys

import SearchMethods
from GridNode import GridNode
from GridReader import GridReader

grid_reader = GridReader()
grid_reader.read_terrain('Terrains/Maze.txt')
grid_reader.add_lateral_neighbors()
# grid_reader.add_diagonal_neighbors()

# for grid_node in grid_reader.grid_nodes:
#     print(grid_node)

source = grid_reader.source_node
destination = grid_reader.destination_node
print("SOURCE: " + str(source))
print("DESTINATION: " + str(destination))

shortest_path, visited, total_cost = SearchMethods.a_star_search(source, destination, GridNode.no_heuristic)
print("Shortest path contained " + str(len(visited)) + " nodes")
for node in shortest_path:
    print(node)

print("Visited " + str(len(visited)) + " nodes")
