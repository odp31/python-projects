import heapq

# 1. Prim's Minimum Spanning Tree

def prim_mst(graph):
  mst = set()
  edges = [(cost, src, dest) for src in graph for dest, cost in graph[src]]
  heapq.heapify(edges)

  while edges:
    cost, src, dest = heapq.heappop(edges)
    if src not in mst or dest not in mst:
      mst.add(src)
      mst.add(dest)
      yield src, dest 

total_cost = sum(cost for cost, _, _ in prim_mst(graph))

# 2. Kruskal's Minnimum Spanning Tree 

def kruskal_mst(graph):
  mst = []
  edges = [(cost, src, dest) for src in graph for dest, cost in graph[src]]
  edges.sort()

  parent = {node: node for node in graph}
  rank = {node: 0 for node in graph}

  def find_parent(node):
    if parent[node] != node:
      parent[node] = find_parent(parent[node])
    return parent[node]

  def union(u,v):
    u_root = find_parent(u)
    v_root = find_parent(v)
    if rank[u_root] < rank[v_root]:
      parent[u_root] = v_root
    elif rank[u_root] > rank[v_root]:
      parent[v_root] = u_root
    else:
      parent[v_root] = u_root
      rank[u_root] += 1 

    for cost, src, dest in edges:
      if find_parent(src) != find_parent(dest):
        mst.append((src, dest, cost))
        union(src, dest)

    return mst 
