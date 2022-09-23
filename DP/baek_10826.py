# 2022/09/23 Baek 9625

n = int(input())
dp = [0 for _ in range(10001)]
dp[1] = 1
dp[2] = 1
def dp_fibo(n):
  for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

  return dp[n]

print(dp_fibo(n))