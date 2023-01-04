# # 2023/01/14 baek 17135

# import sys
# import copy
# from itertools import combinations
# import heapq

# input = sys.stdin.readline

# N, M, D = map(int, input().split())
# board = [list(map(int, input().strip().split())) for _ in range(N)]

# castle = []
# for i in range(M):
#   castle.append((N, i))

# candidates = list(combinations(castle, 3))

# def update_table(board):
#   board.pop()
#   board.insert(0, [0] * M)

# def is_empty(board):
#   for i in range(N):
#     for j in range(M):
#       if board[i][j] == 1:
#         return False
#   return True

# def find_enemy(board, x, y):
#   q = []
#   for row in range(N - 1, -1, -1):
#     for col in range(M):
#       if board[row][col] == 1:
#         dist = abs(x - row) + abs(y - col)
#         if dist <= D:
#           heapq.heappush(q, (dist, col, row))
#   if q:
#     dist, y, x = heapq.heappop(q)
#     return x, y
#   else:
#     return ()
# result = 0

# for candidate in candidates:
#   temp_board = copy.deepcopy(board)
#   cnt = 0
#   while not(is_empty(temp_board)):
#     detected_enemy = set()
#     for x, y in candidate:
#       enemy_index = find_enemy(temp_board, x, y)
#       if enemy_index:
#         detected_enemy.add(enemy_index)
#     for i, j in list(detected_enemy):
#       cnt += 1
#       temp_board[i][j] = 0

#     update_table(temp_board)
#   result = max(result, cnt)

# print(result)


# 백트래킹

import sys
import copy
import heapq

input = sys.stdin.readline

N, M, D = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]

castle = []
for i in range(M):
  castle.append((N, i))

result = 0

def update_table(board):
  board.pop()
  board.insert(0, [0] * M)

def is_empty(board):
  for i in range(N):
    for j in range(M):
      if board[i][j] == 1:
        return False
  return True

def find_enemy(board, x, y):
  q = []
  for row in range(N - 1, -1, -1):
    for col in range(M):
      if board[row][col] == 1:
        dist = abs(x - row) + abs(y - col)
        if dist <= D:
          heapq.heappush(q, (dist, col, row))
  if q:
    dist, y, x = heapq.heappop(q)
    return x, y
  else:
    return ()
result = 0

def back_tracking(start_idx, candidate):
  global result
  if len(candidate) == 3:
    cnt = 0
    temp_board = copy.deepcopy(board)
    while not(is_empty(temp_board)):
      detected_enemy = set()
      for x, y in candidate:
        enemy_index = find_enemy(temp_board, x, y)
        if enemy_index:
          detected_enemy.add(enemy_index)
      for i, j in list(detected_enemy):
        cnt += 1
        temp_board[i][j] = 0
      update_table(temp_board)
    result = max(result, cnt)
  else:
    for i in range(start_idx, len(castle)):
      back_tracking(i + 1, candidate + [castle[i]])

back_tracking(0, [])
print(result)

# BFS 이용코드
import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M, D = map(int, input().split())

matrix = [list(map(int, input().strip().split())) for _ in range(N)]

dx = [0, -1, 0]
dy = [-1, 0, 1]

def kill(archor):
  temp_matrix = [x[:] for x in matrix]
  killed = [[0] * M for _ in range(N)]
  result = 0
  for i in range(N - 1, -1, -1):
    this_turn = []
    for ay in archor:
      dq = deque()
      dq.append((i, ay, 1))
      while dq:
        x, y, d = dq.popleft()
        if temp_matrix[x][y] == 1:
          this_turn.append((x, y))
          if killed[x][y] == 0:
            killed[x][y] = 1
            result += 1
          break
        if d < D:
          for di in range(3):
            nx = x + dx[di]
            ny = y + dy[di]
            if 0 <= nx < N and 0 <= ny < M:
              dq.append((nx, ny, d + 1))

      for x, y in this_turn:
        temp_matrix[x][y] = 0

  return result

answer = 0

archor_pos = list(combinations([i for i in range(M)], 3))
for a in archor_pos:
  answer = max(answer, kill(a))