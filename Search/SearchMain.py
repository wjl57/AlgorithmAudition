from Search import SearchMethods
from Search.GridNode import GridNode
from Search.GridReader import GridReader
from Search.NeighborType import NeighborType

grid_reader = GridReader('Terrains/Maze.txt', NeighborType.LATERAL | NeighborType.DIAGONAL)

# for grid_node in grid_reader.grid_nodes:
#     print(grid_node)

source = grid_reader.source_node
destination = grid_reader.destination_node
print("SOURCE: " + str(source))
print("DESTINATION: " + str(destination))

shortest_path, visited, total_cost = SearchMethods.a_star_search(source, destination, GridNode.euclidean_distance)
print("Shortest path contained " + str(len(shortest_path)) + " nodes")
for node in shortest_path:
    print(node)

print("Visited " + str(len(visited)) + " nodes")
