# 2022/10/24 Baek 1926

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = []

for _ in range(n):
  arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  cnt = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if arr[nx][ny] == 1 and visited[nx][ny] == False:
          visited[nx][ny] = True
          q.append([nx, ny])
          cnt += 1
          
  return cnt
result = 0
cnt = 0
for i in range(n):
  for j in range(m):
    if arr[i][j] == 1 and not visited[i][j]:
      result = max(result, bfs(i,j))
      cnt += 1

print(cnt)
print(result)