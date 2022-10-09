# 2022/10/09 Baek 10835

# top_down
N = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]

for l in range(N - 1, -1, -1):
  for r in range(N - 1, -1, -1):
    if left[l] > right[r]:
      dp[l][r] = dp[l][r + 1] + right[r]
    else:
      dp[l][r] = max(dp[l + 1][r + 1], dp[l + 1][r])

print(dp[0][0])


# dfs 풀이
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
  if x >= n or y >= n:
    return 0

  if dp[x][y] != -1:
    return dp[x][y]

  if left[x] > right[y]:
    dp[x][y] = dfs(x, y + 1) + right[y]
  else:
    discard_left = dfs(x + 1, y)
    discard_both = dfs(x + 1, y + 1)
    dp[x][y] = max(discard_both, discard_left)

  return dp[x][y]

n = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))

dp = [[-1] * (n) for _ in range(n)]
dfs(0,0)
print(dp[0][0])