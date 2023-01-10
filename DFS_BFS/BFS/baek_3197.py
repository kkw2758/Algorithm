# # 2023/01/10 Baek 3197

# import sys
# from collections import deque
# input = sys.stdin.readline

# R, C = map(int, input().split())

# board = [["."] * (C + 2)]
# start_flag = False
# for i in range(1, R + 1):
#   board.append(["."] + list(input().strip()) + ["."])
#   for j in range(C + 2):
#     if board[i][j] == "L":
#       if not start_flag:
#         start_flag = True
#         sx, sy = (i, j)
#       else:
#         ex, ey = (i, j)
# board += [["."] * (C + 2)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def melt_ice():
#   visited = [[0] * (C + 2) for _ in range(R + 2)]
#   q = deque()
#   q.append((0, 0))
#   visited[0][0] = 1
#   target_ice = []
#   while q:
#     x, y = q.popleft()
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if 0 <= nx < R + 2 and 0 <= ny < C + 2 and not visited[nx][ny]:
#         if board[nx][ny] == "X":
#           if x == 0 or x == R + 1 or y == 0 or y == C + 1:
#             continue
#           visited[nx][ny] = 1
#           target_ice.append((nx, ny))
#         else:
#           visited[nx][ny] = 1
#           q.append((nx, ny))

#   for x, y in target_ice:
#     board[x][y] = "."

# def is_possible():
#   q = deque()
#   visited = [[0] * (C + 2) for _ in range(R + 2)]
#   q = deque()
#   q.append((sx, sy))
#   visited[sx][sy] = 1
  
#   while q:
#     x, y = q.popleft()
#     if (x, y) == (ex, ey):
#       return True
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
      
#       if 1 <= nx < R + 1 and 1 <= ny < C + 1 and not visited[nx][ny]:
#         if board[nx][ny] != "X":
#           visited[nx][ny] = 1
#           q.append((nx, ny))
#   return False


# cnt = 0
# while True:
#   if is_possible():
#     break
#   melt_ice()
#   cnt += 1
# print(cnt)


# 2023/01/10 Baek 3197
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def find_swan(queue):
  next_queue = deque()
  while queue:
    x, y = queue.popleft()
    if (x, y) == (swan[1][0], swan[1][1]):
      return True, None
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
        if lake[nx][ny] == "X":
          next_queue.append((nx, ny))
        else:
          queue.append((nx, ny))
        visited[nx][ny] = True

  return False, next_queue

def melt_ice(water):
  next_water = deque()
  while water:
    x, y = water.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < R and 0 <= ny < C:
        if lake[nx][ny] == "X":
          next_water.append((nx, ny))
          lake[nx][ny] = "."

  return next_water

R, C = map(int, input().split())
lake = []
swan = []
water = deque()

for r in range(R):
  lake.append(list(input().strip()))
  for c in range(C):
    if lake[r][c] == "." or lake[r][c] == "L":
      water.append((r, c))
    if lake[r][c] == "L":
      swan.append((r, c))
  
day = -1
visited = [[False] * C for _ in range(R)]
queue = deque()
x, y = swan[0][0], swan[0][1]
queue.append((x, y))
visited[x][y] = True

while True:
  day += 1
  found, next_queue = find_swan(queue)
  if found:
    break
  water = melt_ice(water)
  queue = next_queue

print(day)