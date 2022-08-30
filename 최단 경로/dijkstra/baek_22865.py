# 2022/08/30 Baek 22865

from operator import ne
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
A, B, C = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  D, E, L = map(int, input().split())
  graph[D].append((E, L))
  graph[E].append((D, L))

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

A_distance = dijkstra(A)
B_distance = dijkstra(B)
C_distance = dijkstra(C)
result = [0, 0]
for i in range(1, N + 1):
  if result[0] < min(A_distance[i], B_distance[i], C_distance[i]):
    result[0] = min(A_distance[i], B_distance[i], C_distance[i])
    result[1] = i

print(result[1])