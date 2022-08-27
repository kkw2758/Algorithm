# 2022/08/27 Baek 12786

# import sys
# import heapq

# input = sys.stdin.readline
# INF = int(1e9)
# n = int(input())
# t = int(input())

# graph = [[0] * (n + 1) for _ in range(21)]
# for i in range(1, n + 1):
#   temp = list(map(int, input().rstrip().split()))
#   for j in temp[1:]:
#     graph[j][i] = 1

# t_count = [[INF] * (n + 2) for _ in range(21)]

# def find_door(graph, col):
#   result = []
#   for row in range(len(graph)):
#     if graph[row][col] == 1:
#       result.append((row, col))
  
#   return result

# q = []
# heapq.heappush(q, (0, 1, 1))
# # t_count[1][1] = 0

# while q:
#   t_cnt, x, y = heapq.heappop(q)
#   if y == n + 1:
#     break
#   if t_count[x][y] < t_cnt:
#     continue
#   dx = [0, 1, x, -1]
#   dy = [0, 0, 0, 0]
#   for idx in range(4):
#     nx = x + dx[idx]
#     ny = y + dy[idx]
#     if nx > 20:
#       nx = 20
#     if 1 <= nx <= 20 and 1 <= ny <= 20:
#       if graph[nx][ny] == 1:
#         if t_cnt < t_count[nx][ny]:
#           t_count[nx][ny] = t_cnt
#           t_count[nx][ny + 1] = t_cnt
#           heapq.heappush(q, (t_cnt, nx, ny + 1))

#   for row, col in find_door(graph, y):
#     if t_cnt + 1 < t_count[row][col]:
#       t_count[row][col] = t_cnt + 1
#       t_count[row][col + 1] = t_cnt + 1
#       heapq.heappush(q, (t_cnt + 1, row, col + 1))

# result = INF
# for i in range(1, 21):
#   result = min(result, t_count[i][n + 1])

# if result <= t:
#   print(result)
# else:
#   print(-1)

# for _ in t_count:
#   print(_)



import sys

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
t = int(input())

def find_door(graph, col):
  result = []
  for row in range(len(graph)):
    if graph[row][col] == 1:
      result.append((row, col))
  
  return result


graph = [[0] * (n + 1) for _ in range(21)]
for i in range(1, n + 1):
  temp = list(map(int, input().rstrip().split()))
  for j in temp[1:]:
    graph[j][i] = 1

dp = [[INF] * (n + 2) for _ in range(21)]
# visited = [[False] * (n + 1) for _ in range(21)]
dp[1][1] = 0
for i in range(1, n + 1):
  temp = []
  for j in range(1, 21):
    if dp[j][i] != INF:
      temp.append((j,i))
  for x, y in temp:
    # O
    if graph[x][y] == 1:
      dp[x][y + 1] = min(dp[x][y + 1], dp[x][y])
    # A
    if x < 20 and graph[x + 1][y] == 1:
      dp[x + 1][y] = min(dp[x + 1][y + 1], dp[x][y])
      dp[x + 1][y + 1] = dp[x + 1][y]
    # B
    if x * 2 > 20:
      if graph[20][y] == 1:
        dp[20][y] = min(dp[20][y + 1], dp[x][y])
        dp[20][y + 1] = dp[20][y]
    else:
      if graph[x + x][y] == 1:
        dp[x + x][y] = min(dp[x + x][y + 1], dp[x][y])
        dp[x + x][y + 1] = dp[x + x][y]
    # C
    if x > 1 and graph[x - 1][y] == 1:
      dp[x - 1][y] = min(dp[x - 1][y + 1], dp[x][y])
      dp[x - 1][y + 1] = dp[x - 1][y]
    # T
    for row, col in find_door(graph, y):
      dp[row][col] = min(dp[row][col + 1], dp[x][y] + 1)
      dp[row][col + 1] = dp[row][col]

result = INF
for i in range(1, 21):
  result = min(result, dp[i][n + 1])

if result <= t:
  print(result)
else:
  print(-1)

