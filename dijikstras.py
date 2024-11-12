import heapq

def dijkstra(graph, start):

  # Initialize distances with infinity and set distance to start node to 0 

  distances = {node: float('infinity') for node in graph}
    distances[start] = 0 

  # Priority Queue to hold nodes to explore 
  prirority_queue = [(0, start)]
  while priority_queue:
    current_distance, current_node = heapq.heappop(priority_queue)

  # Nodes can only be added once to the priority queue so we skip if we find a longer path 

  if current_distance > distances[current_node]:
    continue 

  # Explore neightbors 

  for neighbor, weight in graph[current_node].items():
    distance = current_distance + weight 

  # Only consider this new path if its better
  if distance < distances[neighbor]:
    distances[neighbor] = distance 

  heapq.heappush(priority_queue, (distance, neighbor))
    return distances 

# Example Graph grepresented as and adjacency list 
graph = {
  'A' : {'B': 1, 'C': 4}, 
  'B': {'A': 1, 'C': 2, 'D': 5}, 
  'C': {'A': 4, 'B': 2, 'D': 1}, 
  'D': {'B': 5, 'C': 1}
}

# Run algorithm 
start_node = 'A'
distances = dijkstra(graph, start_node)
print(distances) 
