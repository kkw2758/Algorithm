# 2022/08/29 Baek 20007

import heapq
import sys

INF = int(10e9)
input = sys.stdin.readline
N, M, X, Y = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
  A, B, C = map(int, input().split())
  graph[A].append((B, C))
  graph[B].append((A, C))

def dijkstra(start):
  distance = [INF] * N
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

distance = sorted(dijkstra(Y))
cnt = 1
if max(distance) * 2 > X:
  print(-1)
else:
  temp = 0
  for i in range(N):
    if temp + distance[i] * 2 < X:
      temp += (distance[i] * 2)
    else:
      cnt += 1
      temp = (distance[i] * 2)
  print(cnt)