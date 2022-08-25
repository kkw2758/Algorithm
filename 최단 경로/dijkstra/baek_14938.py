# 2022/08/25 Baek 14938

import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(r):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

def dijkstra(start):
  distance = [INF] * (n + 1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for next_node, next_cost in graph[now]:
      cost = dist + next_cost
      if cost > m:
        continue
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))

  result = 0
  for idx in range(len(distance)):
    if distance[idx] != INF:
      result += items[idx]

  return result

result = 0
for i in range(1, n + 1):
  result = max(result, dijkstra(i))

print(result)