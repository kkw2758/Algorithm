# 2023/01/19 Baek 2210

from collections import deque

board = [input().split() for _ in range(5)]
result_set = set()
for _ in board:
  print(_)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  q = deque()
  q.append((x, y, ""))

  while q:
    x, y, string = q.popleft()
    if len(string) == 6:
      result_set.add(string)
      continue

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < 5 and 0 <= ny < 5:
          q.append((nx, ny, string + board[nx][ny]))

for i in range(5):
  for j in range(5):
    bfs(i, j)

print(len(result_set))