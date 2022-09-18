# 2022/09/17 Baek 12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (100001)

for _ in range(N):
  W, V = map(int, input().split())
  for i in range(100000 - W, -1, -1):
    dp[i + W] = max(dp[i + W],dp[i] + V)

print(max(dp[:K + 1]))


# 2차원 배열 knapscak 풀이
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
  stuff.append(list(map(int, input().split())))

for i in range(1, N + 1):
  for j in range(1, K + 1):
    weight = stuff[i][0]
    value = stuff[i][1]

    if j < weight:
      knapsack[i][j] = knapsack[i - 1][j]
    else:
      knapsack[i][j] = max(knapsack[i - 1][j - weight] + value, knapsack[i - 1][j])

print(knapsack[N][K])