# 2022/10/01 Baek 9084

t = int(input())

for _ in range(t):
  n = int(input())
  ary = list(map(int, input().split()))
  m = int(input())

  dp = [0] * (m + 1)
  dp[0] = 1

  for num in ary:
    for i in range(num, m + 1):
      if dp[i - num] != 0 and 0 <= i - num <= m:
        dp[i] += dp[i - num]
  
  print(dp[-1])
