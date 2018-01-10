from collections import defaultdict, deque
from heapq import heappush, heappop

import math

from GridNode import GridNode


def a_star_search(source, destination, heuristic_function):
    visited = set()
    # A priority queue containing tuples of (cost, node) that are not evaluated yet.
    # Initially, only the start node is known.
    frontier = []
    # Mapping from a node to the previous node
    came_from = {}
    heappush(frontier, (heuristic_function(source, destination), source))
    # The cost of getting from the source to that node.
    cost_from_source = defaultdict(lambda: float('inf'))
    cost_from_source[source] = 0
    # For each node, the total cost of getting from the start node to the goal
    # by passing by that node. That value is partly known, partly heuristic.
    total_cost = defaultdict(lambda: float('inf'))
    total_cost[source] = heuristic_function(source, destination)

    while frontier:
        # Get the first node from the priority queue
        (cost, current) = heappop(frontier)
        if current == destination:
            return reconstruct_path(came_from, current, deque())

        # If we've seen the node before, move on
        if current in visited:
            continue

        # Otherwise try to expand the neighbors
        for neighbor in current.neighbors:
            if neighbor not in visited:
                new_source_cost = cost_from_source[current] + current.neighbors[neighbor]
                # Add to the queue if the estimated cost to the neighbor from the source is lower
                if new_source_cost < cost_from_source[neighbor]:
                    # Update costs
                    cost_from_source[neighbor] = new_source_cost
                    new_total_cost = new_source_cost + heuristic_function(neighbor, destination)
                    total_cost[neighbor] = new_total_cost
                    # Update came_from
                    came_from[neighbor] = current
                    # Add the neighbor along with newly estimated cost to the priority queue
                    heappush(frontier, (new_total_cost, neighbor))
    raise Exception("No valid path to destination")


def reconstruct_path(came_from, node, path):
    if node not in came_from:
        return path
    prev_node = came_from[node]
    path.appendleft(prev_node)
    del came_from[node]
    return reconstruct_path(came_from, prev_node, path)


