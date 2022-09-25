# 2022/09/25 Baek 19947

H, Y = map(int, input().split())

dp = [H] * (Y + 1)

for i in range(1, Y + 1):
  dp[i] = int(dp[i - 1] * 1.05)
  
  if i - 3 >= 0:
    dp[i] = max(dp[i], int(dp[i - 3] * 1.2))

  if i - 5 >= 0:
    dp[i] = max(dp[i], int(dp[i - 5] * 1.35))

print(dp[Y])

# 재귀
H, Y = map(int, input().split())

dp = [0] * (Y + 1)
dp[0] = H

def recursive_sol(n):
  if dp[n]:
    return dp[n]
  if n < 3:
    dp[n] = int(recursive_sol(n - 1) * 1.05)
    return dp[n]
  elif 3 <= n < 5:
    dp[n] = max(int(recursive_sol(n - 1) * 1.05), int(recursive_sol(n - 3) * 1.2))
    return dp[n]
  else:
    dp[n] = max(int(recursive_sol(n - 1) * 1.05), int(recursive_sol(n - 3) * 1.2), int(recursive_sol(n - 5) * 1.35))
    return dp[n]

print(recursive_sol(Y))