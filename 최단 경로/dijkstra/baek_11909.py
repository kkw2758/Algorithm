# 2022/08/22 Baek 11909

# 다익스트라 풀이 시간초과..
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[]]
for _ in range(n):
  graph.append([0] + list(map(int, input().split())))

cost_list = [[INF] * (n + 1) for _ in range(n + 1)]

q = []
heapq.heappush(q, (0, 1, 1))
cost_list[1][1] = 0

while q:
  cost, i, j = heapq.heappop(q)
  if cost_list[i][j] < cost:
    continue
  if 1 <= i < n and 1 <= j < n:
    next = [(i, j + 1), (i + 1, j)]
  elif i == n and 1 <= j < n:
    next = [(i, j + 1)]
  elif 1 <= i < n and j == n:
    next = [(i + 1, j)]
  elif i == n and j == n:
    break
  else:
    continue

  for ni, nj in next:
    if graph[i][j] <= graph[ni][nj]:
      new_cost = cost_list[i][j] + graph[ni][nj] - graph[i][j] + 1
      if cost_list[ni][nj] > new_cost:
        cost_list[ni][nj] = new_cost
        heapq.heappush(q, (new_cost, ni, nj))
    else:
      cost_list[ni][nj] = cost_list[i][j]
      heapq.heappush(q, (cost_list[ni][nj], ni, nj))

print(cost_list[n][n])


import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  for j in range(n):
    if i == 0 and j == 0:
      continue
    elif i == 0:
      cost1 = dp[i][j - 1] if board[i][j] < board[i][j - 1] else dp[i][j - 1] + board[i][j] - board[i][j - 1] + 1
      dp[i][j] += cost1
    elif j == 0:
      cost2 = dp[i - 1][j] if board[i][j] < board[i - 1][j] else dp[i - 1][j] + board[i][j] - board[i - 1][j] + 1
      dp[i][j] += cost2
    else:
      cost1 = dp[i][j - 1] if board[i][j] < board[i][j - 1] else dp[i][j - 1] + board[i][j] - board[i][j - 1] + 1
      cost2 = dp[i - 1][j] if board[i][j] < board[i - 1][j] else dp[i - 1][j] + board[i][j] - board[i - 1][j] + 1
      dp[i][j] = min(cost1, cost2)

print(dp[n - 1][n - 1])
    