# 2023/01/12 Baek 1986

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]

kx = [-2, -2, -1, -1, 1, 1, 2, 2]
ky = [-1, 1, -2, 2, -2, 2, -1, 1]
qx = [-1, -1, -1, 0, 0, 1, 1, 1]
qy = [-1, 0, 1, -1, 1, -1, 0, 1]

queens = list(map(int, input().split()))
knights = list(map(int, input().split()))
pawns = list(map(int, input().split()))

for i in range(pawns[0]):
  x, y = pawns[1 + i * 2] - 1, pawns[2 + i * 2] - 1
  board[x][y] = "P"

for i in range(knights[0]):
  x, y = knights[1 + i * 2] - 1, knights[2 + i * 2] - 1
  board[x][y] = "K"

for i in range(queens[0]):
  x, y = queens[1 + i * 2] - 1, queens[2 + i * 2] - 1
  board[x][y] = "Q"
  for i in range(8):
    idx = 1
    while True:
      nx = x + qx[i] * idx
      ny = y + qy[i] * idx
      if not(0 <= nx < n and 0 <= ny < m):
        break
      if board[nx][ny] == "K" or board[nx][ny] == "P":
        break
      board[nx][ny] = "Q"
      idx += 1


for i in range(knights[0]):
  x, y = knights[1 + i * 2] - 1, knights[2 + i * 2] - 1
  for i in range(8):
    nx = x + kx[i]
    ny = y + ky[i]
    if 0 <= nx < n and 0 <= ny and board[nx][ny] == 0:
      board[nx][ny] = "K"

result = 0
for i in range(n):
  for j in range(m):
    if board[i][j] == 0:
      result += 1

print(result)
