import heapq
import time
from ex1 import Graph
import random

def dijkstra_slow(graph, source):
    # Time complexity: O(V^2)
    distances = {node_id: float('inf') for node_id in graph.nodes}
    distances[source.id] = 0
    visited = set()
    
    # node id
    node_map = graph.nodes
    
    while len(visited) < len(graph.nodes):
        # min distance search
        min_dist = float('inf')
        min_node_id = None
        
        for node_id in graph.nodes:
            if node_id not in visited and distances[node_id] < min_dist:
                min_dist = distances[node_id]
                min_node_id = node_id
        
        if min_node_id is None:
            break
        
        visited.add(min_node_id)
        
        # update neighbors
        for neighbor_id, weight in graph.adjacency_list[min_node_id]:
            if neighbor_id not in visited:
                new_dist = distances[min_node_id] + weight
                if new_dist < distances[neighbor_id]:
                    distances[neighbor_id] = new_dist
    
    return distances


def dijkstra_fast(graph, source):
    # Time complexity: O((V+E)log V)
    distances = {node_id: float('inf') for node_id in graph.nodes}
    distances[source.id] = 0
    pq = [(0, source.id)]
    visited = set()
    
    while pq:
        dist, node_id = heapq.heappop(pq)
        
        if node_id in visited:
            continue
        
        visited.add(node_id)
        
        for neighbor_id, weight in graph.adjacency_list[node_id]:
            if neighbor_id not in visited:
                new_dist = dist + weight
                if new_dist < distances[neighbor_id]:
                    distances[neighbor_id] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor_id))
    
    return distances


# test
def test_performance():
    graph = Graph()
    graph.importFromFile('random.dot')
    
    if not graph.nodes:
        print("Could not load random.dot")
        return
    
    nodes = list(graph.nodes.values())
    
    slow_times = []
    for node in nodes:
        start = time.time()
        dijkstra_slow(graph, node)
        end = time.time()
        slow_times.append(end - start)
    
    print("SLOW Dijkstra (O(V^2)):")
    print(f"  Average time: {sum(slow_times)/len(slow_times):.6f} seconds")
    print(f"  Max time: {max(slow_times):.6f} seconds")
    print(f"  Min time: {min(slow_times):.6f} seconds")
    
    fast_times = []
    for node in nodes:
        start = time.time()
        dijkstra_fast(graph, node)
        end = time.time()
        fast_times.append(end - start)
    
    print("\nFAST Dijkstra (O((V+E)log V)):")
    print(f"  Average time: {sum(fast_times)/len(fast_times):.6f} seconds")
    print(f"  Max time: {max(fast_times):.6f} seconds")
    print(f"  Min time: {min(fast_times):.6f} seconds")
    
    # plot histogram
    try:
        import matplotlib.pyplot as plt
        
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.hist(slow_times, bins=20, edgecolor='black')
        plt.title('Slow Dijkstra (O(V²))')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Frequency')
        
        plt.subplot(1, 2, 2)
        plt.hist(fast_times, bins=20, edgecolor='black')
        plt.title('Fast Dijkstra (O((V+E)log V))')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Frequency')
        
        plt.tight_layout()
        plt.show()
        
        print("\nRESULTS DISCUSSION:")
        print("=" * 50)
        print("The fast Dijkstra implementation using a heap is significantly")
        print("faster than the slow version. This is because the slow version")
        print("uses linear search (O(V)) to find the minimum distance node,")
        print("while the heap version can find it in O(log V) time.")
        print("\nThe heap version is especially beneficial for large graphs")
        print("because the time saved grows with the number of nodes.")
        print("For dense graphs, the difference is even more pronounced.")
        
    except ImportError:
        print("\nNote: matplotlib not installed. Skipping histogram.")


if __name__ == "__main__":
    test_performance()