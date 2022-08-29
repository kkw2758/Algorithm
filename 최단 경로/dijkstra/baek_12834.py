# 2022/08/29 Baek 12834

import sys
import heapq

INF = int(1e9)

input = sys.stdin.readline
N, V, E = map(int, input().split())
A, B = map(int, input().split())
H = list(map(int, input().split()))

graph = [[] for _ in range(V + 1)]
for _ in range(E):
  a, b, l = map(int, input().split())
  graph[a].append((b, l))
  graph[b].append((a, l))

def dijkstra(start):
  distance = [INF] * (V + 1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for next_node, next_dist in graph[now]:
      cost = dist + next_dist
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))

  return distance

result = 0
for h in H:
  distance = dijkstra(h)
  if distance[A] == INF:
    result -= 1
  else:
    result += distance[A]

  if distance[B] == INF:
    result -= 1
  else:
    result += distance[B]

print(result)