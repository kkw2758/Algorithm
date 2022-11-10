# 2022/11/10 Baek 17141

from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
virus_index = []


for i in range(N):
  arr.append(list(map(int, input().split())))
  for j in range(N):
    if arr[i][j] == 2:
      virus_index.append((i, j))

def is_full():
  for i in range(N):
    for j in range(N):
      if visited[i][j] == False and arr[i][j] != 1:
        return False

  return True

def bfs(candidate):
  q = deque()
  for i, j in candidate:
    q.append((i, j, 0))
    visited[i][j] = True

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]
  while q:
    x, y, cnt = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        # 벽이 아니고 방문을 안했을때
        if arr[nx][ny] != 1 and visited[nx][ny] == False:
          visited[nx][ny] = True
          q.append((nx, ny, cnt + 1))

  return cnt

result = int(1e9)
candidates = list(combinations(virus_index, M))
for candidate in candidates:
  visited = [[False] * N for _ in range(N)]
  cnt = bfs(candidate)
  flag = is_full()
  if flag == True:
    result = min(result, cnt)

if result == int(1e9):
  print(-1)
else:
  print(result)