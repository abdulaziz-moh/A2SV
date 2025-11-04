from collections import defaultdict

class Graph:
    """
    A class to represent a directed or undirected graph using adjacency lists.

    Attributes
    ----------
    graph : defaultdict(list)
        A dictionary containing each node as a key and a list of its neighbors as value.
    """

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Add an edge from node u to node v.
        
        Parameters
        ----------
        u : any
            The starting node of the edge.
        v : any
            The ending node of the edge.
        """
        self.graph[u].append(v)

    def dfs(self, start, visited=None):
        """
        Perform Depth-First Search (DFS) starting from a given node.

        Parameters
        ----------
        start : any
            The starting node for DFS traversal.
        visited : set, optional
            Set of visited nodes to avoid cycles (default is None).

        Returns
        -------
        list
            List of nodes in the order they were visited.
        """
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        return result

    def depth_limited_search(self, start, goal, limit):
        """
        Perform Depth-Limited Search (DLS) to find a path from start to goal with depth limit.

        Parameters
        ----------
        start : any
            The starting node.
        goal : any
            The goal node to reach.
        limit : int
            The maximum depth to search.

        Returns
        -------
        list or None
            List of nodes representing the path from start to goal if found, else None.
        """
        def recursive_dls(node, goal, depth, path, visited):
            visited.add(node)
            path.append(node)

            if node == goal:
                return path

            if depth <= 0:
                path.pop()
                return None

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    result = recursive_dls(neighbor, goal, depth-1, path, visited)
                    if result:
                        return result

            path.pop()
            return None

        return recursive_dls(start, goal, limit, [], set())


# ------------------ Example Usage ------------------

# Create a graph
g = Graph()
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')]
for u, v in edges:
    g.add_edge(u, v)

# DFS traversal
print("DFS Traversal from A:", g.dfs('A'))

# Depth-Limited Search
print("Depth-Limited Search (A -> F, limit=2):", g.depth_limited_search('A', 'F', 2))
print("Depth-Limited Search (A -> F, limit=3):", g.depth_limited_search('A', 'F', 3))


# ✅ Explanation:

# Graph Class
# Uses an adjacency list (dictionary of lists) to store graph connections.

# DFS (dfs method)

# Recursively visits a node and all its unvisited neighbors.

# Returns the order in which nodes were visited.

# Depth-Limited Search (depth_limited_search method)

# Recursively searches for a goal node, but does not exceed the depth limit.

# Returns the path to the goal if it exists; otherwise, returns None.

# Example Usage

# DFS prints all nodes reachable from 'A'.

# DLS tries to find 'F' from 'A' with a depth limit, demonstrating how the limit affects the search.