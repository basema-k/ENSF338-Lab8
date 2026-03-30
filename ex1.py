class GraphNode:
    def __init__(self, data):
        self.data = data
        self.adjacent = {}  


class Graph:
    def __init__(self):
        self.nodes = {} 

    # 1. Required methods
    def addNode(self, data):
        if data not in self.nodes:
            node = GraphNode(data)
            self.nodes[data] = node
            return node
        return self.nodes[data]

    def removeNode(self, node):
        if node.data in self.nodes:
            # Remove edges pointing to this node
            for n in self.nodes.values():
                if node in n.adjacent:
                    del n.adjacent[node]
            del self.nodes[node.data]
