# 2022/08/27 Baek 22116

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
graph = [[]]
n = int(input())
for _ in range(n):
  graph.append([0] + list(map(int, input().rstrip().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

distance = [[INF] * (n + 1) for _ in range(n + 1)]

result = INF
q = []
heapq.heappush(q, (0, 1, 1))
distance[1][1] = 0

while q:
  max_incline, x, y = heapq.heappop(q)
  if distance[x][y] < max_incline:
    continue
  if x == n and y == n:
    break
  for idx in range(4):
    nx = x + dx[idx]
    ny = y + dy[idx]
    if 1 <= nx <= n and 1 <= ny <= n:
      if distance[nx][ny] > max(max_incline, abs(graph[x][y] - graph[nx][ny])):
        distance[nx][ny] = max(max_incline, abs(graph[x][y] - graph[nx][ny]))
        heapq.heappush(q, (distance[nx][ny], nx, ny))

print(distance[n][n])
