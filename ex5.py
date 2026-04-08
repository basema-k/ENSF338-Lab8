
from ex1 import Graph

# Q1
# Topological sort can be implemented using DFS.
# When we run DFS and append a node to the result after visiting all its neighbors,
# reversing the result gives a valid topological order.
# This works because all successors are added before their predecessors.


def isdag(self):
    visited = set()
    stack = set()

    def visit(node):
        visited.add(node)
        stack.add(node)

        for neigh in node.adjacent:
            if neigh not in visited:
                if not visit(neigh):
                    return False
            elif neigh in stack:
                return False

        stack.remove(node)
        return True

    for node in self.nodes.values():
        if node not in visited:
            if not visit(node):
                return False

    return True


def toposort(self):
    if not self.isdag():
        return None

    visited = set()
    result = []

    def visit(node):
        visited.add(node)
        for neigh in node.adjacent:
            if neigh not in visited:
                visit(neigh)
        result.append(node.data)

    for node in self.nodes.values():
        if node not in visited:
            visit(node)

    return result[::-1]


Graph.isdag = isdag
Graph.toposort = toposort