import networkx as nx
import heapq


# Define a priority queue that uses heapq
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task, priority):
        heapq.heappush(self.queue, (priority, task))

    def dequeue(self):
        return heapq.heappop(self.queue)

    def is_empty(self):
        return not bool(self.queue)


# Dijkstra's algorithm
def dijkstra(graph, start_node):
    visited = set()
    distances = {node: float("infinity") for node in graph.nodes}
    distances[start_node] = 0
    priority_queue = PriorityQueue()
    # Add the start node
    priority_queue.enqueue(start_node, 0)

    # Loop until the queue is empty
    while not priority_queue.is_empty():
        current_distance, current_node = priority_queue.dequeue()

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.enqueue(neighbor, distance)

    return distances


if __name__ == "__main__":
    G = nx.Graph()
    G.add_edge("A", "B", weight=1)
    G.add_edge("B", "C", weight=2)
    G.add_edge("A", "C", weight=5)
    G.add_edge("C", "D", weight=1)
    G.add_edge("A", "D", weight=8)

    shortest_paths = dijkstra(G, "A")

    # Print the shortest paths
    for node, distance in shortest_paths.items():
        print(f"Shortest path from A to {node}: {distance}")
