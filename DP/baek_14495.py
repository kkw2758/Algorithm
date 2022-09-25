# 2022/09/25 Baek 14495

n = int(input())
dp = [0] * 117
dp[1] = 1
dp[2] = 1
dp[3] = 1

def similar_fibo(n):
  if dp[n]:
    return dp[n]
  else:
    dp[n] = similar_fibo(n - 1) + similar_fibo(n - 3)
    return dp[n]

print(similar_fibo(n))