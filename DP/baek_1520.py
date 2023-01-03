# 2022/12/30 Baek 1520

import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(sx, sy):
  if dp[sx][sy] != -1:
    return dp[sx][sy]

  if (sx, sy) == (0, 0):
    dp[sx][sy] = 1
    return 1
  
  ways = 0
  for i in range(4):
      nx = sx + dx[i]
      ny = sy + dy[i]
      if 0 <= nx < m and 0 <= ny < n and graph[sx][sy] < graph[nx][ny]:
          ways += dfs(nx, ny)
  
  dp[sx][sy] = ways
  return dp[sx][sy]


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]


print(dfs(m - 1, n - 1))