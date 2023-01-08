# 2023/01/02 Baek 2589

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
lands = []
for i in range(n):
  board.append(list(input().strip()))
  for j in range(m):
    if board[i][j] == "L":
      lands.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  visited = [[False] * m for _ in range(n)]
  q = deque()
  q.append((x, y, 0))
  visited[x][y] = True

  while q:
    x, y, cnt = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if not visited[nx][ny] and board[nx][ny] == "L":
          visited[nx][ny] = True
          q.append((nx, ny, cnt + 1))

  return cnt

result = 0
for lx, ly in lands:
  result = max(result, bfs(lx, ly))

print(result)