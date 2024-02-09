import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for i in range(vertices)]
        
    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))
     
    def dijkstra(self, src):
        min_heap = [(0, src)]
        distances = [float('inf')] * self.V
        distances[src] = 0
        
        while min_heap:
            dist, current_vertex = heapq.heappop(min_heap)
            
            for neighbor, weight in self.graph[current_vertex]:
                distance_through_v = dist + weight
                
                if distance_through_v < distances[neighbor]:
                    distances[neighbor] = distance_through_v
                    heapq.heappush(min_heap, (distance_through_v, neighbor))
                    
        return distances

# Приклад використання
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

distances = g.dijkstra(0)
print("Відстані від вершини 0 до інших:")
for i in range(9):
    print(f"0 -> {i} = {distances[i]}")