# 2023/01/08 Baek 14925

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
board = [[0] * (N + 1)]
board += [[0] + list(map(int, input().split())) for _ in range(M)]
dp = [[0] * (N + 1) for _ in range(M + 1)]


for i in range(1, M + 1):
  for j in range(1, N + 1):
    if board[i][j] == 0:
      dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

result = 0
for row in dp:
  result = max(result, max(row))

print(result)