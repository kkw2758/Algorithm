# 2022/08/24 Baek 1753

import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]
distance = [INF for _ in range(v + 1)]

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

q = []
heapq.heappush(q, (0, k))
distance[k] = 0

while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist:
    continue
  for next_node, next_cost in graph[now]:
    cost = dist + next_cost
    if cost < distance[next_node]:
      distance[next_node] = cost
      heapq.heappush(q, (cost, next_node))

for dist in distance[1:]:
  if dist == INF:
    print("INF")
  else:
    print(dist)