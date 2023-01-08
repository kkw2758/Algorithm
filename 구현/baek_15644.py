#2022/12/28 baek 15644

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []

for i in range(N):
  board.append(list(input().rstrip()))
  for j in range(M):
    if board[i][j] == "R":
      rx, ry = i, j
    elif board[i][j] == "B":
      bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction = ["U", "D", "L", "R"]

def bfs(rx, ry, bx, by):
  q = deque()
  visited = []
  q.append((rx, ry, bx, by, ""))
  visited.append((rx, ry, bx, by))

  while q:
    rx, ry, bx, by, result = q.popleft()
    
    if board[rx][ry] == "O":
      print(len(result))
      print(result)
      return
       
    for i in range(4):
      nrx, nry = rx, ry 
      while True:
        nrx += dx[i]
        nry += dy[i]
        if board[nrx][nry] == "#":
          nrx -= dx[i]
          nry -= dy[i]
          break
        if board[nrx][nry] == "O":
          break

      nbx, nby = bx, by
      while True:
        nbx += dx[i]
        nby += dy[i]
        if board[nbx][nby] == "#":
          nbx -= dx[i]
          nby -= dy[i]
          break
        if board[nbx][nby] == "O":
          break

      if board[nbx][nby] == "O":
        continue
      
      if (nrx, nry) == (nbx, nby):
        if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
          nrx -= dx[i]
          nry -= dy[i]
        else:
          nbx -= dx[i]
          nby -= dy[i]

      if (nrx, nry, nbx, nby) not in visited:
        q.append((nrx, nry, nbx, nby, result + direction[i]))
        visited.append((nrx, nry, nbx, nby))
  print(-1)

bfs(rx, ry, bx, by)