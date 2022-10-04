# 2022/10/04 Baek 13398

n = int(input())
ary = list(map(int, input().split()))
dp = [[0] * n for _ in range(2)]

dp[0][0] = ary[0]
dp[1][0] = ary[0]

for i in range(1, n):
  dp[0][i] = max(dp[0][i - 1] + ary[i], ary[i])
  dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + ary[i])

print(max(max(dp[0]), max(dp[1])))