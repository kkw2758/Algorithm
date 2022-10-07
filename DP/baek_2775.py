# 2022/10/07 Baek 2775

T = int(input())
for _ in range(T):
  k = int(input())
  n = int(input())

  dp = [[0] * (n + 1) for _ in range(k + 1)]
  for i in range(1, n + 1):
    dp[0][i] = i

  for i in range(1, k + 1):
    for j in range(1, n + 1):
      temp = 0
      for l in range(j + 1):
        temp += dp[i - 1][l] 
      
      dp[i][j] = temp

  print(dp[k][n])