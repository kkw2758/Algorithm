# 2023/01/05 Baek 2234

import sys
from collections import deque
input = sys.stdin.readline

#서 북 동 남
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
  q = deque()
  q.append([x, y])
  visited[x][y] = 1
  cnt = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
        if i == 0:
          if 1 & board[x][y]:
            continue
        elif i == 1:
          if 2 & board[x][y]:
            continue
        elif i == 2:
          if 4 & board[x][y]:
            continue
        elif i == 3:
          if 8 & board[x][y]:
            continue
        visited[nx][ny] = 1
        q.append([nx, ny])
        cnt += 1

  return cnt

N, M = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
result1, result2, result3 = 0, 0, 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            result1 += 1
            result2 = max(result2, bfs(i, j))

for i in range(M):
  for j in range(N):
    num = 1
    while num < 9:
      if num & board[i][j]:
          visited = [[0] * N for _ in range(M)]
          board[i][j] -= num
          result3 = max(result3, bfs(i, j))
          board[i][j] += num
      num *= 2

print(result1)
print(result2)
print(result3)

# visited = [[0] * N for _ in range(M)]
# result1 = 0
# result2 = 0
# for i in range(M):
#   for j in range(N):
#     if visited[i][j] == 0:
#       result1 += 1
#       result2 = max(result2, bfs(i, j))

# result3 = 0
# for i in range(M):
#   for j in range(N):
#     num = 1
#     while num < 9:
#       if num & board[i][j]:
#         visit = [[0] * N for _ in range(M)]
#         board[i][j] -= num
#         result3 = max(result3, bfs(i, j))
#         board[i][j] += num
#       num *= 2

# print(result1)
# print(result2)
# print(result2)