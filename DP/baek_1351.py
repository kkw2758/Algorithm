# 2022/10/08 Baek 1351

def infinite(n):
  if n in dp:
    return dp[n]
  else:
    dp[n] = infinite(n//P) + infinite(n//Q)
    return dp[n]

N, P, Q = map(int, input().split())
dp = dict()
dp[0] = 1

infinite(N)
print(dp[N])