# 2022/09/01 Baek 23801

import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))
  graph[v].append((u, w))

x, z = map(int, input().split())
P = int(input())
middle_node = list(map(int, input().rstrip().split()))

def dijkstra(start):
  distance = [INF] * (N + 1)
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

result = INF
x_to = dijkstra(x)
z_to = dijkstra(z)

for p in middle_node:
  result = min(result, x_to[p] + z_to[p])
  
if result >= INF:
  print(-1)
else:
  print(result)