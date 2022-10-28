# 2022/10/27 Baek 17404
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
rgb = []
for _ in range(n):
  rgb.append(list(map(int, input().split())))

ans = INF
for i in range(3):
  dp = [[INF] * 3 for _ in range(n)]
  dp[0][i] = rgb[0][i]
  for j in range(1, n):
    dp[j][0] = rgb[j][0] + min(dp[j - 1][1], dp[j - 1][2])
    dp[j][1] = rgb[j][1] + min(dp[j - 1][0], dp[j - 1][2])
    dp[j][2] = rgb[j][2] + min(dp[j - 1][0], dp[j - 1][1])

  for j in range(3):
    if i != j:
      ans = min(ans, dp[-1][j])

print(ans)

#dp 배열크기를 재선언 하지 않는 효율적인 코드
import sys
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
rgb = []
for _ in range(N):
  rgb.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(2)]
ans = INF

for k in range(3):
  dp[0][0], dp[0][1], dp[0][2] = INF, INF, INF
  dp[0][k] = rgb[0][k]

  for i in range(1, N):
    dp[1][0] = min(dp[0][1], dp[0][2]) + rgb[i][0]
    dp[1][1] = min(dp[0][0], dp[0][2]) + rgb[i][1]
    dp[1][2] = min(dp[0][0], dp[0][1]) + rgb[i][2]

    dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]

  ans = min(ans, dp[0][(k + 1) % 3], dp[0][(k + 2) % 3])

print(ans)