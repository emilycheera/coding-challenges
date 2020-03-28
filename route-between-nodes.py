
from collections import deque

class Node():
    """A node object."""

    def __init__(self, data, adjacent=None):
        """Instantiate a node object."""

        adjacent = adjacent or set()
        assert isinstance(adjacent, set), "Adjacent must be a set."
        
        self.adjacent = adjacent
        self.data = data


class Graph():
    """A graph object."""

    def __init__(self):
        """Instantiate a graph object."""
        self.nodes = set()

    def add(self, node):
        """Add a node to the graph."""
        self.nodes.add(node)

    @staticmethod
    def find_route(node1, node2):
        """Return True if there's a route between node1 and node2."""

        # Use a queue instead of a stack because BFS will find shortest route.
        to_visit = deque()
        to_visit.append(node1)
        seen = set()
        seen.add(node1)

        while to_visit:
            node = to_visit.popleft()
            if node == node2:
                return True
            for node in (node.adjacent - seen):
                to_visit.append(node)
                seen.add(node)

        return False





