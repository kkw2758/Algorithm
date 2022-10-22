# 2022/10/22 Baek 2573
from collections import deque

def bfs(x, y):
  q = deque()
  q.append([x, y])
  visited[x][y] = True
  while q:
    x, y = q.popleft()
    visited[x][y] = True
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if visited[nx][ny] == False and arr[nx][ny] != 0:
          q.append([nx, ny])
          visited[nx][ny] = True
        elif arr[nx][ny] == 0:
          count[x][y] += 1


n, m = map(int, input().split())
arr = []

for _ in range(n):
  arr.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
result = 0
check = False
while True:
  visited  = [[False] * m for _ in range(n)]
  count = [[0] * m for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(m):
      if arr[i][j] != 0 and visited[i][j] == False:
        bfs(i, j)
        cnt += 1

  for i in range(n):
    for j in range(m):
      arr[i][j] = max(arr[i][j] - count[i][j], 0)

  if cnt >= 2:
    check = True
    break
  elif cnt == 0:
    break
  result += 1
print(result if check else 0)