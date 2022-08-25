# 2022/08/25 Baek 4485

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dijkstra(start_x, start_y):
  q = []
  distance = [[INF] * n for _ in range(n)]
  heapq.heappush(q, (graph[start_x][start_y], start_x, start_y))
  distance[start_x][start_y] = graph[start_x][start_y]
  while q:
    total_cost, x, y = heapq.heappop(q)
    if distance[x][y] < total_cost:
      continue
    for idx in range(4):
      nx = x + dx[idx]
      ny = y + dy[idx]
      if 0 <= nx < n and 0 <= ny < n:
        next_cost = total_cost + graph[nx][ny]
        if next_cost < distance[nx][ny]:
          distance[nx][ny] = next_cost
          heapq.heappush(q, (next_cost, nx, ny))
  return distance[n-1][n-1]

cnt = 0
while True:
  cnt += 1
  n = int(input())
  if n == 0:
    break
  graph = []

  for _ in range(n):
    graph.append(list(map(int, input().split())))

  print("Problem {}: {}".format(cnt,dijkstra(0,0)))