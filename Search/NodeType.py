from enum import Enum


class NodeType(Enum):
    NORMAL = 1
    SOURCE = 2
    DESTINATION = 3
    WALL = 4
