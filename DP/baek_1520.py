# 2022/12/30 Baek 1520

import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
  if dp[x][y] != -1:
    return dp[x][y]

  if (x, y) == (0, 0):
    return 1

  ways = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < M and 0 <= ny < N:
      if board[x][y] < board[nx][ny]:
        ways += dfs(nx, ny)

  dp[x][y] = ways
  return dp[x][y]


# def dfs(x, y):
#   if dp[x][y] != -1:
#     return dp[x][y]

#   if x == M - 1 and  y == N - 1:
#     return 1

#   dp[x][y] = 0

#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]

#     if 0 <= nx < M and 0 <= ny < N:
#       if board[x][y] > board[nx][ny]:
#         dp[x][y] += dfs(nx, ny)

#   return dp[x][y]

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
print(dfs(M - 1, N - 1))

for _ in dp:
  print(_)