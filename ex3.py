class GraphNode:
    def __init__(self, data):
        self.data = data
        self.adjacent = {}  # neighbor -> weight


    def __repr__(self):
        return f"GraphNode({self.data})"

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def makeSet(self, node):
        self.parent[node] = node
        self.rank[node] = 0

    def find(self, node):
        # Path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, n1, n2):
        root1 = self.find(n1)
        root2 = self.find(n2)

        if root1 == root2:
            return False  # cycle detected

        # Union by rank
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True

class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, data):
        if data in self.nodes:
            return self.nodes[data]
        node = GraphNode(data)
        self.nodes[data] = node
        return node

    def addEdge(self, n1, n2, weight=1):
        if n1 is None or n2 is None:
            return
        if n2 not in n1.adjacent:
            n1.adjacent[n2] = weight
            n2.adjacent[n1] = weight

    # kruskal 
    def mst(self):
        mst_graph = Graph()

        # Initialize Union-Find
        uf = UnionFind()
        for node in self.nodes.values():
            uf.makeSet(node)
            mst_graph.addNode(node.data)

        # Collect all edges (avoid duplicates)
        edges = []
        seen = set()

        for n1 in self.nodes.values():
            for n2, weight in n1.adjacent.items():
                if (n2, n1) not in seen:
                    edges.append((weight, n1, n2))
                    seen.add((n1, n2))

        # Sort edges by weight
        edges.sort(key=lambda x: x[0])

        # Process edges
        for weight, n1, n2 in edges:
            if uf.union(n1, n2):  # no cycle
                new_n1 = mst_graph.nodes[n1.data]
                new_n2 = mst_graph.nodes[n2.data]
                mst_graph.addEdge(new_n1, new_n2, weight)

        return mst_graph

