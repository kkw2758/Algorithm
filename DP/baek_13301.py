# 2022/09/24 Baek 13301

n = int(input())
dp = [0] * (81)
dp[1] = 1
dp[2] = 1

def dynamic_fibo(n):
  for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

dynamic_fibo(n)
print(dp[n] * 4 + dp[n - 1] * 2)