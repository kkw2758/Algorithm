# 2022/08/24 Baek 1504

import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]


for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
  distance = [INF for i in range(n + 1)]
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for next_node, next_cost in graph[now]:
      cost = dist + next_cost
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))
  
  return distance

one_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)
result = min(one_distance[v1] + v1_distance[v2] + v2_distance[n], one_distance[v2] + v2_distance[v1] + v1_distance[n])
print(result if result < INF else -1)