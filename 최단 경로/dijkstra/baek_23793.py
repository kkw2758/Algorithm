# 2022/08/31 Baek 23793

import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

x, y, z = map(int, input().split())

def dijkstra(start, Flag):
  distance = [INF] * (N + 1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for next_node, next_dist in graph[now]:
      if next_node == y and Flag:
        continue
      cost = dist + next_dist
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))

  return distance

x_distance = dijkstra(x, False)
x_true_distance = dijkstra(x, True)
y_distance = dijkstra(y, False)
if x_distance[y] + y_distance[z] >= INF:
  print(-1, end = " ")
else:
  print(x_distance[y] + y_distance[z], end = " ")
if x_true_distance[z] == INF:
  print(-1, end = " ")
else:
  print(x_true_distance[z], end = " ")