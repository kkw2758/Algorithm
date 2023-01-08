# 2022/12/29 Baek 1915

n, m = map(int, input().split())
board = [[0] * (m + 1)] + [[0] + list(map(int, list(input().rstrip()))) for _ in range(n)]
dp = [[0] * (m + 1) for i in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, m + 1):      
    if board[i][j] == 0:
      dp[i][j] = 0
    else: # board[i][j] == 1
      dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

result = 0
for row in dp:
  result = max(result, max(row))

print(result ** 2)