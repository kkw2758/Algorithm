# 2022/09/06 Baek 1992

from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

INF = int(1e9)
graph = []
tomatoes = []
for i in range(N):
  row = list(map(int, input().split()))
  for j in range(len(row)):
    if row[j] == 1:
      tomatoes.append([i, j])
  graph.append(row)

distance = [[INF] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(tomatoes):
  queue = deque()
  for tomato in tomatoes:
    queue.append((tomato[0], tomato[1]))
    distance[tomato[0]][tomato[1]] = 0

  while queue:
    x, y = queue.popleft()
    for idx in range(4):
      nx = x + dx[idx]
      ny = y + dy[idx]
      
      if 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] != -1:
          if distance[nx][ny] > distance[x][y] + 1:
            distance[nx][ny] = distance[x][y] + 1
            graph[nx][ny] = 1
            queue.append((nx, ny))

bfs(tomatoes)

def check():
  max_value = 0
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 0:
        return -1
      elif graph[i][j] == 1:
        max_value = max(max_value, distance[i][j])

  return max_value

print(check())