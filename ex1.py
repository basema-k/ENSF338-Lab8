class GraphNode:
    def __init__(self, data):
        self.data = data
        self.adjacent = {}  # neighbor - weight

    def __repr__(self):
        return f"GraphNode({self.data})"


class Graph:
    def __init__(self):
        self.nodes = {}  # data string - GraphNode

    # part 1
    def addNode(self, data):
        if data in self.nodes:
            return self.nodes[data]
        node = GraphNode(data)
        self.nodes[data] = node
        return node

    def removeNode(self, node):
        if node.data not in self.nodes:
            return

        for other in self.nodes.values():
            if node in other.adjacent:
                del other.adjacent[node]

        del self.nodes[node.data]

    def addEdge(self, n1, n2, weight=1):
        if n1 is None or n2 is None:
            return

        if n2 not in n1.adjacent:
            n1.adjacent[n2] = weight
            n2.adjacent[n1] = weight

    def removeEdge(self, n1, n2):
        if n2 in n1.adjacent:
            del n1.adjacent[n2]
        if n1 in n2.adjacent:
            del n2.adjacent[n1]

    # part 2
    def importFromFile(self, file):
        try:
            with open(file, "r") as f:
                lines = f.readlines()

            self.nodes.clear()

            if not lines[0].strip().startswith("strict graph"):
                return None

            for line in lines[1:]:
                line = line.strip()

                if line == "}" or line == "":
                    continue

                if not line.endswith(";"):
                    return None
                line = line[:-1]

                if "--" not in line:
                    return None

                parts = line.split("--")
                left = parts[0].strip()
                right_part = parts[1].strip()

                weight = 1
                if "[" in right_part:
                    node2, attr = right_part.split("[")
                    node2 = node2.strip()
                    attr = attr.strip("]")

                    if "weight=" in attr:
                        try:
                            weight = int(attr.split("=")[1])
                        except:
                            return None
                else:
                    node2 = right_part.strip()

                n1 = self.addNode(left)
                n2 = self.addNode(node2)

                self.addEdge(n1, n2, weight)

            return self

        except:
            return None