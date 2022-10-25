# 2022/10/25 Baek 1937
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def dfs(x, y):
  if dp[x][y]:
    return dp[x][y]
  dp[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if arr[x][y] < arr[nx][ny]:
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
  return dp[x][y]

answer = 0
for i in range(n):
  for j in range(n):
    answer = max(answer, dfs(i,j))

print(answer)