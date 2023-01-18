# 2023/01/18 Baek 4963

import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def dfs(x, y):
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w:
      if board[nx][ny] == 1 and not visited[nx][ny]:
        visited[nx][ny] = 1
        dfs(nx, ny)

while True:
  w, h = map(int, input().split())
  if (w, h) == (0, 0):
    break

  board = [list(map(int, input().strip().split())) for _ in range(h)]
  visited = [[False] * w for _ in range(h)]
  cnt = 0
  for i in range(h):
    for j in range(w):
      if not visited[i][j] and board[i][j] == 1:
        dfs(i, j)
        cnt += 1

  print(cnt)