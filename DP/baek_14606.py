# 2022/09/24 Baek 14606

n = int(input())
dp = [0] * (n + 1)
dp[1] = 0

for i in range(2, n + 1):
  for j in range(1, int(i//2) + 1):
    dp[i] = max(dp[i],(j * (i - j)) + dp[max(j, (i - j))])

print(dp[n])