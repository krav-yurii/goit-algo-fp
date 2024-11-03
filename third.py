import heapq

class Graph:
    def __init__(self):
        self.nodes = set()  
        self.edges = {}    

    def add_node(self, value):
        """Додає вершину до графа."""
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        """Додає ребро до графа."""
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

def dijkstra(graph, start):
    """Алгоритм Дейкстри для знаходження найкоротших шляхів від вершини start."""
    distances = {vertex: float('inf') for vertex in graph.nodes}
    distances[start] = 0

    heap = [(0, start)] 

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


def main():
    graph = Graph()

    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'Z', 6),
        ('E', 'Z', 3),
    ]

    for from_node, to_node, weight in edges:
        graph.add_edge(from_node, to_node, weight)

    start_vertex = 'A'

    distances = dijkstra(graph, start_vertex)

    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex in sorted(distances):
        print(f"Відстань до {vertex}: {distances[vertex]}")

if __name__ == "__main__":
    main()
