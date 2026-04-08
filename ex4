
import time
from ex1 import Graph

class Graph2:
    def __init__(self):
        self.nodes = []
        self.index = {}
        self.matrix = []

    def addNode(self, data):
        if data in self.index:
            return data
        self.index[data] = len(self.nodes)
        self.nodes.append(data)

        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * len(self.nodes))

        return data

    def addEdge(self, n1, n2, weight=1):
        if n1 not in self.index or n2 not in self.index:
            return
        i = self.index[n1]
        j = self.index[n2]
        self.matrix[i][j] = weight
        self.matrix[j][i] = weight

    def dfs(self):
        visited = set()
        result = []

        def visit(i):
            visited.add(i)
            result.append(self.nodes[i])
            for j in range(len(self.nodes)):
                if self.matrix[i][j] != 0 and j not in visited:
                    visit(j)

        for i in range(len(self.nodes)):
            if i not in visited:
                visit(i)

        return result


# extend original Graph class
def dfs_graph(self):
    visited = set()
    result = []

    def visit(node):
        visited.add(node)
        result.append(node.data)
        for neigh in node.adjacent:
            if neigh not in visited:
                visit(neigh)

    for node in self.nodes.values():
        if node not in visited:
            visit(node)

    return result


Graph.dfs = dfs_graph


# performance test
g = Graph()
g.importFromFile("random.dot")

g2 = Graph2()
for n in g.nodes:
    g2.addNode(n)
for node in g.nodes.values():
    for neigh, w in node.adjacent.items():
        g2.addEdge(node.data, neigh.data, w)

times1 = []
times2 = []

for _ in range(10):
    t0 = time.time()
    g.dfs()
    times1.append(time.time() - t0)

    t0 = time.time()
    g2.dfs()
    times2.append(time.time() - t0)

print("Graph DFS:", min(times1), max(times1), sum(times1)/len(times1))
print("Graph2 DFS:", min(times2), max(times2), sum(times2)/len(times2))

# Graph (adj list) is faster because it only visits existing edges.
# Graph2 (matrix) checks all possible edges, so it is slower.
# With ~1000 nodes, matrix checks ~1,000,000 cells while list only checks actual edges.