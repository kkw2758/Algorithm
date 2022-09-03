# 2022/09/03 Baek 17626
import sys

n = int(input())
limit_number = 100000
sys.setrecursionlimit(limit_number)

dp = [-1 for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1

def func(n):
  if dp[n] != -1:
    return dp[n]
  result = int(1e9)
  j = 1
  while (j ** 2) <= n: 
    result = min(result, 1 + func(n - j ** 2))
    j += 1
  dp[n] = result
  return result

print(func(n))

N = int(input())
dp = [0,1]

for i in range(2, N+1):
    min_value = 1e9
    j = 1

    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1

    dp.append(min_value + 1)
result2 = dp

print(dp[N])