# 2022/09/24 Baek 16395

n, k = map(int, input().split())
dp = [[]] + [[0] + [1] * i for i in range(1, n + 1)]

for i in range(3, n + 1):
  for j in range(2, i):
    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

for _ in dp:
  print(_)

print(dp[n][k])