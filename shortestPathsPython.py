# 1. Dijkistra's Algorithm 

# finds shortest path from a starting node to all other nodes in a weighted graph 

import heapq

def dijkstra(graph, start):
  # Initialize distances with infinity and set distance to start node to 0 
  distances = {node: float('infinity) for node in graph}
  distances[start] = 0

  priority_queue = [(0, start)]
    while priority_queue:
      current_distance, current_node = heapq.heappop(priority_queue)

      if current_distance > distances[current_node]:
                continue
      for neightbor, weight in graph[current_node].items():
                distance = current_distance + weight 

                if distance < distances[neighbor]: distances[neighbor] = distance
  
  heapq.heappush(priority_queue, (distance, neighbor))
    return distances 



graph = {
  'A' : {'B': 1, 'C': 4}, 
  'B': {'A' : 1, 'C' : 2, 'D' : 5},
  'C': {'A': 4, 'B': 2, 'D': 1}, 
  'D': {'B': 5, 'C': 1}
}

# Run algorithm 
start_node = 'A'
distances = dijkstra(graph,start_node)
print(distances) 



# 2. Breadth First Search (BFS): explores all nodes at present depth level before moving on to nodes at next depth level 

from collections import deque 
def bfs(graph, start):
  visited = set()          # set is used to keep track of visited nodes to avoid processing same node multiple times 
  queue = deqeue([start])  # queue to keep track of nodes to visit; deque from collections module is used for efficient popping from the front 
  visited.add(start)

  while queue: 
    vertex = queue.popleft()
    print(vertext, end = " ")

    for neighbor in graph[vertex]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
        
# Example graph represented as an adjacency list where each node points to a list of its neighbors 
graph = {
  'A': ['B', 'C'], 
  'B': ['A', 'D', 'E'], 
  'C': ['A', 'F'], 
  'D': ['B'], 
  'E': ['B', 'F'], 
  'F': ['C', 'E']
}
bfs(graph, 'A')

# given output should be A B C D E F 


# 3. Depth First Search (DFS): used to search graph data structures by exploring as far as possible along each branch before backtracking 
def dfs(graph, start, visited = None):
  if visited is None:
    visited = set()      # Used to keep track of visited nodes to avoid reprocessing a node 
  visited.add(start)
  print(start, end = " ")

  for neighbor in graph[start]:
    if neighbor not in visited:
      dfs(graph, neighbor, visited) # Recursive traversal; starting from start node, visit each node and recursively explore neighbors 

graph = {
  'A': ['B', 'C'], 
  'B': '['A', 'D', 'E'],
  'C': ['A', 'F']
  'D': ['B'], 
  'E': ['B', 'F'], 
  'F': ['C', 'E']
}
dfs(graph, 'A')

