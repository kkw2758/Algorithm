# 2022/09/23 Baek 9625

k = int(input())
dp = [[] for _ in range(k + 1)]
dp[1] = (0,1)
for i in range(2, k + 1):
  dp[i] = (dp[i - 1][1], dp[i - 1][0] + dp[i - 1][1])

print(dp[k][0], dp[k][1])