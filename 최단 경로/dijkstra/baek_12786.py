# 2022/08/27 Baek 12786

# import sys
# input = sys.stdin.readline

# N = int(input())
# K = int(input())
# dp = [[float('inf')] * 21 for i in range(N + 1)]
# hole = [[1]]
# dp[0][1] = 0

# for i in range(N):
#     a = list(map(int,input().split()))
#     a = a[1:]
#     hole.append(a)

# for i in range(N):
#     for k in hole[i]:
#         dp[i + 1][k] = min(dp[i + 1][k], dp[i][k])
#         if k < 20:
#           dp[i + 1][k + 1] = min(dp[i + 1][k + 1], dp[i][k])
#         dp[i + 1][min(k * 2, 20)] = min(dp[i + 1][min(k * 2, 20)], dp[i][k])
#         if k > 1:
#           dp[i + 1][k - 1] = min(dp[i + 1][k - 1], dp[i][k])
#         for j in range(1, 21):
#           dp[i + 1][j] = min(dp[i + 1][j], dp[i][k] + 1)

# ans = float('inf')
# for k in hole[-1]:
#     ans = min(dp[-1][k], ans)
# if ans > K:
#   ans = -1
# print(ans)

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

# t_count = [[INF] * (n + 1) for _ in range(21)]

# def find_door(graph, col):
#   result = []
#   for row in range(len(graph)):
#     if graph[row][col] == 1:
#       result.append((row, col))
  
#   return result

# q = []
# heapq.heappush(q, (0, 1, 0))
# t_count[1][0] = 0

# while q:
#   t_cnt, x, y = heapq.heappop(q)
#   if y == n:
#     break
#   if t_count[x][y] < t_cnt:
#     continue

#   dx = [0, 1, x, -1]
#   dy = [1, 1, 1, 1]
#   for idx in range(4):
#     nx = x + dx[idx]
#     ny = y + dy[idx]
#     if nx > 20:
#       nx = 20
#     if 1 <= nx <= 20 and 1 <= ny <= 20:
#       if graph[nx][ny] == 1:
#         if t_cnt < t_count[nx][ny]:
#           t_count[nx][ny] = t_cnt
#           heapq.heappush(q, (t_cnt, nx, ny))

#   for row, col in find_door(graph, y + 1):
#     if t_cnt + 1 < t_count[row][col]:
#       t_count[row][col] = t_cnt + 1
#       heapq.heappush(q, (t_cnt + 1, row, col))

# result = INF
# for i in range(1, 21):
#   result = min(result, t_count[i][n])

# if result <= t:
#   print(result)
# else:
#   print(-1)

# for _ in t_count:
#   print(_)