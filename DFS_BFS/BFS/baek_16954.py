# 2022/11/16 Baek 16954

from collections import deque

board = [list(input()) for _ in range(8)]

def move_wall():
  for row in range(7, -1, -1):
    for col in range(8):
      if row == 7:
        if board[row][col] == "#":
          board[row][col] = "."
      else:
        if board[row][col] == "#":
          board[row][col] = "."
          board[row + 1][col] = "#"

def bfs():
  dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
  dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
  q = deque()
  q.append((7, 0))
  while q:
    visited = [[False] * 8 for _ in range(8)]
    len_q = len(q)
    candidates = []
    for i in range(len_q):
      x, y = q.popleft()

      if (x, y) == (0, 7):
        return 1

      for idx in range(9):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == "." and not visited[nx][ny]:
          candidates.append((nx, ny))
          
    move_wall()

    for candidate in candidates:
      if board[candidate[0]][candidate[1]] == ".":
        visited[candidate[0]][candidate[1]] = True
        q.append(candidate)
        

  return 0

print(bfs())


# 2022/11/16 Baek 16954

from collections import deque

board = [list(input()) for _ in range(8)]

def move_wall():
  for row in range(7, -1, -1):
    for col in range(8):
      if row == 7:
        if board[row][col] == "#":
          board[row][col] = "."
      else:
        if board[row][col] == "#":
          board[row][col] = "."
          board[row + 1][col] = "#"

def bfs():
  dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
  dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
  q = deque()
  q.append((7, 0))

  while q:
    len_q = len(q)
    candidates = []
    for i in range(len_q):
      x, y = q.popleft()
      if (x, y) == (0, 7):
        return 1
      for idx in range(9):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] != "#":
          candidates.append((nx, ny))
    move_wall()
    
    candidates = list(set(candidates))
    for candidate in candidates:
      if board[candidate[0]][candidate[1]] == ".":
        q.append(candidate)

  return 0

print(bfs())