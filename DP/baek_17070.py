# 2022/09/28 Baek 17070

import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dp = [[[0 for _ in range(n)] for _ in range(n)] for i in range(3)]

dp[0][0][1] = 1
# dp[i][j][k] i > 가로 세로 대각
for i in range(2, n):
  if graph[0][i] == 0:
    dp[0][0][i] = dp[0][0][i - 1]

for i in range(1, n):
  for j in range(2, n):
    if graph[i][j] == 0 and graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
      dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
    if graph[i][j] == 0:
      dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
      dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(sum(dp[i][n - 1][n - 1] for i in range(3)))


import sys
input = sys.stdin.readline

def dfs(pos):
  global cnt
  x, y, z = pos

  if x == n - 1 and y == n - 1:
    cnt += 1
    return
  
  if x + 1 < n and y + 1 < n:
    if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
      dfs((x + 1, y + 1, 2))

  if z == 0 or z == 2:
    if y + 1 < n:
      if graph[x][y + 1] == 0:
        dfs((x, y + 1, 0))

  if z == 1 or z == 2:
    if x + 1 < n:
      if graph[x + 1][y] == 0:
        dfs((x + 1, y, 1))

cnt = 0
n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dfs((0, 1, 0))

print(cnt)