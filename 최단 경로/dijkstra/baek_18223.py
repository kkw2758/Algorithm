# 2022/08/26 Baek 18223

import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

v, e, p = map(int, input().split())
graph = [[] for i in range(v + 1)]


for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

def dijkstra(start):
  distance = [INF] * (v + 1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for next_node, next_cost in graph[now]:
      cost = dist + next_cost
      if cost <= distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))

  return distance

one_to_any = dijkstra(1)
p_to_any = dijkstra(p)

if one_to_any[p] + p_to_any[v] == one_to_any[v]:
  print("SAVE HIM")
else:
  print("GOOD BYE")