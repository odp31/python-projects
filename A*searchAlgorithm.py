# uses a heuristic function to guide search towards goal node 

import heapq

def a_star_search(graph, start, goal, heuristic):
  open_set = [(heuristic(start, goal), start)]
  closed_set = set()
  came_from = {}
  g_score = {node: float('infinity') for node in graph}
  g_score[start] = 0

  while open_set:
    current = heapq.heappop(open_set)[1]
    if current == goal:
      path = []
      while current in came_from:
        path.append(current)
        current = came_from[current]
      path.append(start)
      path.reverse()
      return path 

    closed_set.add(current)
    for neighbor, cost in graph[current].items():
      tentative_g_score = g_score[current] + cost 
      if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
        came_from[neighbor] = current
        g_score[neighbor] = tentative_g_score 
        f_score = g_score[neighbor] + heuristic(neighbor, goal)
        heapq.heappush(open_set, (f_score, neighbor))

return None 
