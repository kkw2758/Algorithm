# 2022/09/25 Baek 13699

n = int(input())

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
  result = 0
  for j in range(i):
    result += dp[j] * dp[i - j - 1]
  dp[i] = result

print(dp[n])