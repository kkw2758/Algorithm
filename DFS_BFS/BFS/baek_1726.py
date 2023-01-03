# 2023/01/03 Baek 1726

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(M)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[[-1] * N for _ in range(M)] for _ in range(4)]

def bfs():
  q = deque()
  q.append((sx - 1, sy - 1, sd - 1))
  visited[sd - 1][sx - 1][sy - 1] = 0

  while q:
    x, y, d = q.popleft()
    if (x, y, d) == (ex - 1, ey - 1, ed - 1):
      return visited[ed - 1][ex - 1][ey - 1]
    # if d % 2 == 0:
    #   for i in range(2, 4):
    #     if visited[(d + i) % 4][x][y] == -1:
    #       visited[(d + i) % 4][x][y] = visited[d][x][y] + 1
    #       q.append((x, y, (d + i) % 4))
    #   if visited[(d + 1) % 4][x][y] == -1:
    #     visited[(d + 1) % 4][x][y] = visited[d][x][y] + 2
    #     q.append((x, y, (d + 1) % 4))
    # else:
    #   for i in range(1, 3):
    #     if visited[(d + i) % 4][x][y] == -1:
    #       visited[(d + i) % 4][x][y] = visited[d][x][y] + 1
    #       q.append((x, y, (d + i) % 4))
    #   if visited[(d - 1) % 4][x][y] == -1:
    #     visited[(d - 1) % 4][x][y] = visited[d][x][y] + 2
    #     q.append((x, y, (d - 1) % 4))
    for i in range(4):
      if d != i and visited[i][x][y] == -1:
        if (d == 0 and i == 1) or (d == 1 and i == 0) or (d == 2 and i == 3) or (d == 3 and i == 2):
          visited[i][x][y] = visited[d][x][y] + 2
          q.append((x, y, i))
        else:
          visited[i][x][y] = visited[d][x][y] + 1
          q.append((x, y, i))
    nx = x
    ny = y
    for _ in range(3):
      nx += dx[d]
      ny += dy[d]
      if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 1:
        break
      if 0 <= nx < M and 0 <= ny < N and visited[d][nx][ny] == -1 and board[nx][ny] == 0:
        visited[d][nx][ny] = visited[d][x][y] + 1
        q.append((nx, ny, d))


print(bfs())
for _ in visited:
  print(_)