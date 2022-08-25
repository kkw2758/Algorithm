# 2022/08/25 Baek 2665

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[]]
for _ in range(n):
  graph.append([0] + list(map(int, list(input().rstrip()))))

change_count_list = [[INF] * (n + 1) for _ in range(n + 1)]

q = []
heapq.heappush(q, (0, 1, 1))
change_count_list[1][1] = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:
  change_count, x, y  = heapq.heappop(q)
  if change_count_list[x][y] < change_count:
    continue
  for idx in range(4):
    nx = x + dx[idx]
    ny = y + dy[idx]
    if 1 <= nx <= n and 1 <= ny <= n:
      if graph[nx][ny] == 0:
        next_change_count = change_count + 1
      else:
        next_change_count = change_count
      if next_change_count < change_count_list[nx][ny]:
        change_count_list[nx][ny] = next_change_count
        heapq.heappush(q, (next_change_count, nx, ny))

print(change_count_list[n][n])