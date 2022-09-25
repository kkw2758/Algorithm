# 2022/09/25 Baek 10211

T = int(input())
for _ in range(T):
  N = int(input())
  dp = list(map(int, input().split()))
  for i in range(1, N):
    dp[i] = max(dp[i], dp[i - 1] + dp[i])

  print(max(dp))