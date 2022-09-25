# 2022/09/25 Baek 15489

R, C, W = map(int, input().split())

dp = [[]] + [[0] * (i + 1) for i in range(1, R + W)]
dp[1][1] = 1
for i in range(2, R + W):
  for j in range(1, i + 1):
    left = 0
    right = 0
    if j - 1 > 0:
      left = dp[i - 1][j - 1]
    if j <= i - 1:
      right = dp[i - 1][j]
    dp[i][j] = left + right


result = 0
cnt = 1
for row in range(R, R + W):
  for col in range(cnt):
    result += dp[row][C + col]
  cnt += 1

print(result)