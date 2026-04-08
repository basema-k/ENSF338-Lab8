
import time
import heapq
import matplotlib.pyplot as plt
from ex1 import Graph

# Q1
# 1. Use a list and scan it every time (slow because O(n))
# 2. Use a priority queue / heap (fast because O(log n))


# slow (linear)
def slowSP(self, start):
    dist = {node: float('inf') for node in self.nodes.values()}
    dist[start] = 0
    visited = set()

    while len(visited) < len(self.nodes):
        current = None
        min_dist = float('inf')

        for node in self.nodes.values():
            if node not in visited and dist[node] < min_dist:
                min_dist = dist[node]
                current = node

        if current is None:
            break

        visited.add(current)

        for neigh, w in current.adjacent.items():
            if dist[current] + w < dist[neigh]:
                dist[neigh] = dist[current] + w

    return dist


# fast (heap)
def fastSP(self, start):
    dist = {node: float('inf') for node in self.nodes.values()}
    dist[start] = 0
    
    counter = 0
    pq = [(0, counter, start)]

    while pq:
        d, _, current = heapq.heappop(pq)
        
        if d > dist[current]:
            continue

        for neigh, w in current.adjacent.items():
            new_d = dist[current] + w
            if new_d < dist[neigh]:
                dist[neigh] = new_d
                counter += 1
                heapq.heappush(pq, (new_d, counter, neigh))

    return dist


Graph.slowSP = slowSP
Graph.fastSP = fastSP


# test
g = Graph()
g.importFromFile("random.dot")

slow_times = []
fast_times = []

for node in g.nodes.values():
    t0 = time.time()
    g.slowSP(node)
    slow_times.append(time.time() - t0)

    t0 = time.time()
    g.fastSP(node)
    fast_times.append(time.time() - t0)


print("SlowSP:", min(slow_times), max(slow_times), sum(slow_times)/len(slow_times))
print("FastSP:", min(fast_times), max(fast_times), sum(fast_times)/len(fast_times))

plt.figure()
plt.hist(slow_times)
plt.title("SlowSP Times")
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.hist(fast_times)
plt.title("FastSP Times")
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.show()

# Q4
# The fastSP histogram is concentrated at lower times, while slowSP is more spread out and higher.
# This shows fastSP is more efficient because it uses a heap (O(log n)),
# while slowSP scans all nodes (O(n)), making it slower, especially on larger graphs.