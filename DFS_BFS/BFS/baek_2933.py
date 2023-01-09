# 2023/01/09 Baek 2933

import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().strip().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited = set()
  visited.add((x, y))

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in visited:
        if board[nx][ny] == "x":
          visited.add((nx, ny))
          q.append((nx, ny))

  visited = list(visited)
  visited.sort(reverse=True)
  
  return visited

for i in range(N):
  # 하나 부시기
  if i % 2 == 0:
    for j in range(C):
      if board[R - heights[i]][j] == "x":
        board[R - heights[i]][j] = "."
        broken_x, broken_y = R - heights[i], j
        break
  else:
    for j in range(C - 1, -1, -1):
      if board[R - heights[i]][j] == "x":
        board[R - heights[i]][j] = "."
        broken_x, broken_y = R - heights[i], j
        break

  flag = False
  for k in range(4):
    new_broken_x = broken_x + dx[k]
    new_broken_y = broken_y + dy[k]
    if 0 <= new_broken_x < R and 0 <= new_broken_y < C:
      if board[new_broken_x][new_broken_y] == "x":
        cluster = bfs(new_broken_x, new_broken_y)
        if cluster[0][0] != R - 1:
          # 공중에 뜬 친구 찾으면
          flag = True
          break
  
  for _ in board:
    print(_)

  if flag == True:
    print(cluster)
    floor_index = [-1] * C
    for x, y in cluster:
      floor_index[y] = max(floor_index[y], x)
    print(floor_index)
    down_cnt = 100
    for col in range(len(floor_index)):
      if floor_index[col] != -1:
        cnt = 0
        for row in range(floor_index[i] + 1, R):
          if board[row][col] == "x":
            break
          cnt += 1
        print(col, cnt)
        down_cnt = min(down_cnt, cnt)
    print(down_cnt)