# 2022/11/13 Baek 1600

from collections import deque
import sys

input = sys.stdin.readline
K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
hx = [-2, -2, -1, -1, 1, 1, 2, 2]
hy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs():
  visited = [[[-1] * (K + 1) for _ in range(W)] for _ in range(H)]
  q = deque()
  q.append((0, 0, K))
  visited[0][0][K] = 0
  while q:
    x, y, cnt = q.popleft()
    if (x, y) == (H - 1, W - 1):
      return visited[H - 1][W - 1][cnt]
    if cnt > 0:
      for i in range(8):
        nx = x + hx[i]
        ny = y + hy[i]
        if (0 <= nx < H and 0 <= ny < W) and visited[nx][ny][cnt - 1] == -1 and arr[nx][ny] == 0:
          visited[nx][ny][cnt - 1] = visited[x][y][cnt] + 1
          q.append((nx, ny, cnt - 1))

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < H and 0 <= ny < W) and visited[nx][ny][cnt] == -1 and arr[nx][ny] == 0:
        visited[nx][ny][cnt] = visited[x][y][cnt] + 1
        q.append((nx, ny, cnt))

  return -1

print(bfs())