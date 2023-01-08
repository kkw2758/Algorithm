# 2023/01/07 Baek 2636

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [[0] * (M + 2)]
board += [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
board += [[0] * (M + 2)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
  q = deque()
  q.append((0, 0))
  visited = [[False] * (M + 2) for _ in range(N + 2)]
  visited[0][0] = True
  cheese_cnt = 0
  # target_cheeses = []
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N + 2 and 0 <= ny < M + 2 and not visited[nx][ny]:
        if board[nx][ny] == 1:
          # target_cheeses.append((nx, ny))
          board[nx][ny] = 0
          cheese_cnt += 1
          visited[nx][ny] = True
          continue
        visited[nx][ny] = True
        q.append((nx, ny))

  return cheese_cnt

result1 = 0
result2 = 0

while True:
  cheese_cnt = bfs()
  if cheese_cnt == 0:
    break
  result2 = cheese_cnt
  result1 += 1

print(result1)
print(result2)