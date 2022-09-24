# 2022/09/24 Baek 14916

INF = int(1e9)

n = int(input())
dp = [INF] * (n + 1)
dp[0] = 0
for i in [2, 5]:
  for j in range(i, n + 1):
    dp[j] = min(dp[j - i] + 1, dp[j])

if dp[n] != INF:
  print(dp[n])
else:
  print(-1)