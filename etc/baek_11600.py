# 2022/09/15 Baek 11660

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ary = [[]]
for _ in range(N):
  ary.append([0] + list(map(int, input().rstrip().split())))

# dp[x][y] >> ary[0][0] 에서부터 ary[x][y] 까지의 합
dp = [[0] * (N + 1) for _ in range(N + 1)]
for row in range(1, N + 1):
  for col in range(1, N + 1):
    dp[row][col] = dp[row - 1][col] + sum(ary[row][1: col + 1])


for _ in dp:
  print(_)

for _ in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  result = 0
  for row in range(x1 -1 , x2):
    result += sum(ary[row][y1 - 1:y2])

  print(result)