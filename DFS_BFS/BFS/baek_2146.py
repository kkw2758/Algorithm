# 2022/12/09 baek 2146
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
islands = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(start_x, start_y):
  island = []
  stack = []
  stack.append((start_x, start_y))
  island.append((start_x, start_y))
  visited[start_x][start_y] = True

  while stack:
    x, y = stack.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] == 1 and visited[nx][ny] == False:
          visited[nx][ny] = True
          stack.append((nx, ny))
          island.append((nx, ny))

  return island

for i in range(N):
  for j in range(N):
    if board[i][j] == 1 and visited[i][j] == False:
      islands.append(dfs(i, j))

def bfs(start):
  visited = [[False] * N for _ in range(N)]
  q = deque()
  
  for x, y in start:
    visited[x][y] = True
    q.append((x, y, 0))

  while q:
    x, y, cnt = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        if visited[nx][ny] == False:
          if board[nx][ny] == 1:
            return cnt
          visited[nx][ny] = True
          q.append((nx, ny, cnt + 1))

result = int(1e9)
for island in islands:
  result = min(result, bfs(island))

print(result)

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, col):
  q = deque()
  q.append((x, y))
  data[x][y] = col
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 1:
        data[nx][ny] = col
        q.append((nx, ny))

def check_bridge(x, y, col):
  q = deque()
  q.append((x, y))
  visited = [[0] * n for _ in range(n)]
  visited[x][y] = 1
  while q:
    x, y = q.popleft()
    if 0 < data[x][y] < col:
      return visited[x][y] - 2
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and data[nx][ny] != col and not visited[nx][ny]:
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))
      
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

col = 2
ans = list()
for i in range(n):
  for j in range(n):
    if data[i][j] == 1:
      bfs(i, j, col)
      col += 1 

col = 2
for i in range(n):
  for j in range(n):
    if data[i][j] != 0:
      a = check_bridge(i, j, data[i][j])
      if a != None:
        ans.append(a)

print(min(ans))
for _ in data:
  print(_)
print(ans)