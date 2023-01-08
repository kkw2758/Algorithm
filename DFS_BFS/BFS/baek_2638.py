# 2023/01/08 Baek 2638

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque()
  q.append((0, 0))
  visited[0][0] = True
  board[0][0] = 2
  target_index = []
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        if board[nx][ny] == 1:
          visited[nx][ny] = True
          target_index.append((nx, ny))
          continue
        visited[nx][ny] = True
        if board[nx][ny] != 2:
          board[nx][ny] = 2
        q.append((nx, ny))

  delete_index = []
  for x, y in target_index:
    cnt = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if board[nx][ny] == 2:
        cnt += 1
        if cnt >= 2:
          delete_index.append((x, y))
          break

  if delete_index:
    for x, y in delete_index:
      board[x][y] = 2
    return True

  return False

cnt = 0
while True:
  visited = [[False] * M for _ in range(N)]
  if bfs():
    cnt += 1
  else:
    print(cnt)
    break


import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque()
  q.append((0, 0))
  visited = [[False] * M for _ in range(N)]
  visited[0][0] = True
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        if board[nx][ny]:
          board[nx][ny] += 1
        else:
          visited[nx][ny] = True
          q.append((nx, ny))


cnt = 0
while True:
  flag = False
  bfs()
  for i in range(N):
    for j in range(M):
      if board[i][j] > 2:
        board[i][j] = 0
        flag = True
      elif board[i][j] == 2:
        board[i][j] = 1

  if flag == False:
    break
  cnt += 1

print(cnt)
