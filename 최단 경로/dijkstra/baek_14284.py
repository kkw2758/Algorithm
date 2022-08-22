# 2022/08/22 Baek 14284

import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, end):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    if now == end:
      return
    for next_node, next_dist in graph[now]:
      cost = dist + next_dist
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))

INF = int(1e9)
n, m = map(int, input().split())

result = INF
graph = [[] for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

s, t = map(int, input().split())

dijkstra(s, t)
print(distance[t])