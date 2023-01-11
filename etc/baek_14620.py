# # 2023/01/11 Baek 14620

# import sys
# input = sys.stdin.readline

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]

# min_value = int(1e9)

# def dfs(depth, flower_index, start):
#   global min_value
#   if depth == 3:
#     result = 0
#     visited = [[0] * N for _ in range(N)]
#     for i in range(3):
#       x, y = flower_index[i]
#       visited[x][y] = 1
#       result += board[x][y]
#       for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if not(0 <= nx < N and 0 <= ny < N) or visited[nx][ny] == 1:
#           return
#         visited[nx][ny] = 1
#         result += board[nx][ny]

#     min_value = min(min_value, result)
#     return

#   for i in range(start, N * N):
#     row = i // N
#     col = i % N
#     dfs(depth + 1, flower_index + [[row, col]], i + 1)


# dfs(0, [], 0)
# print(min_value)


# 2023/01/11 Baek 14620

import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

min_value = int(1e9)

def dfs(depth, start):
  global min_value
  if depth == 3:
    result = 0

    for i in range(N):
      for j in range(N):
        if visited[i][j] == 1:
          result += board[i][j]

    min_value = min(min_value, result)
    return

  for i in range(start, N * N):
    x = i // N
    y = i % N
    temp = []
    if visited[x][y] == 1:
      continue
    else: # visited[x][y] == 0
      visited[x][y] = 1
      temp.append((x, y))
      cnt = 0
      for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        # 범위 밖으로 나가면 꽃 죽음
        if not(0 <= nx < N and 0 <= ny < N):
          break
        # 꽃끼리 닿아도 꽃 죽음
        if visited[nx][ny] == 1:
          break
        visited[nx][ny] = 1
        temp.append((nx, ny))
        cnt += 1

      if cnt == 4:
        dfs(depth + 1, i + 1)
        
      for x, y in temp:
        visited[x][y] = 0


dfs(0, 0)
print(min_value)