# 2022/10/05 Baek 15486

import sys
input = sys.stdin.readline

N = int(input())
ary = [[]]
for _ in range(N):
  ary.append(list(map(int, input().split())))

dp = [0] * (N + 1)
max_value = 0
for i in range(1, N + 1):
  max_value = max(max_value, dp[i - 1])
  if i + ary[i][0] > N + 1:
    continue
  else:
    j = i + ary[i][0] - 1
    dp[j] = max(dp[j], max_value + ary[i][1])
    print(i, dp)

print(max(dp))