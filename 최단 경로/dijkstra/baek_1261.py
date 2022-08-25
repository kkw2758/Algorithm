# 2022/08/25 Baek 1261

import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline
m, n = map(int, input().split())  # 가로 세로
graph = [[]]
for _ in range(n):
  graph.append([0] + list(map(int, list(input().rstrip()))))

break_count_list = [[INF] * (m + 1) for _ in range(n + 1)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dijkstra(start_x, start_y):
  q = []
  heapq.heappush(q, (0, start_x, start_y))  # break_count,
  break_count_list[start_x][start_y] = 0

  while q:
    break_count, x, y = heapq.heappop(q)
    if break_count_list[x][y] < break_count:
      continue
    for idx in range(4):
      nx = x + dx[idx]
      ny = y + dy[idx]
      if (1 <= nx <= n and 1 <= ny <= m):
        if graph[nx][ny] == 0:
          new_break_count = break_count
        else:
          new_break_count = break_count + 1
        if new_break_count < break_count_list[nx][ny]:
          break_count_list[nx][ny] = new_break_count
          heapq.heappush(q, (new_break_count, nx, ny))

dijkstra(1,1)
print(break_count_list[n][m])