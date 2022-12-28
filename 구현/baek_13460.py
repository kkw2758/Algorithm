#2022/12/28 baek 13460

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(input()))
  for j in range(m):
    if graph[i][j] == "R":
      rx, ry = i, j
    elif graph[i][j] == "B":
      bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by):
  q = deque()
  q.append((rx, ry, bx, by))
  visited = []
  visited.append((rx, ry, bx, by))
  count = 0
  
  while q:
    for _ in range(len(q)):
      rx, ry, bx, by = q.popleft()
      if count > 10:
        print(-1)
        return
      if graph[rx][ry] == "O":
        print(count)
        return
      for i in range(4):
        nrx = rx
        nry = ry
        while True:
          nrx += dx[i]
          nry += dy[i]
          if graph[nrx][nry] == "#":
            nrx -= dx[i]
            nry -= dy[i]
            break
          if graph[nrx][nry] == "O":
            break
        nbx = bx
        nby = by
        while True:
          nbx += dx[i]
          nby += dy[i]
          if graph[nbx][nby] == "#":
            nbx -= dx[i]
            nby -= dy[i]
            break
          if graph[nbx][nby] == "O":
            break
        if graph[nbx][nby] == "O":
          continue
      
        if nrx == nbx and nry == nby:
          if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
            nrx -= dx[i]
            nry -= dy[i]
          else:
            nbx -= dx[i]
            nby -= dy[i]
        
        if (nrx, nry, nbx, nby) not in visited:
          q.append((nrx, nry, nbx, nby))
          visited.append((nrx, nry, nbx, nby))
    count += 1
  print(-1)

bfs(rx, ry, bx, by)

# 빨간색 구슬과 파란색 구슬의 시작 좌표를 저장한다.
# 구슬을 BFS를 통해서 4방향으로 굴린다.
# 만약 다음 이동경로가 벽이라면 앞으로 가지 못한다.
# 만약 구슬의 현재 위치가 구멍이라면 구멍위치의 구슬 색을 판별한다.
# 만약 구멍위치의 구슬이 파란색이라면 큐에 추가하지 않고 넘어간다.
# 만약 구멍위치의 구슬이 빨간색이라면 1을 출력하고 종료

import sys
from collections import deque
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
q = deque()
visited = []
q.append((rx, ry, bx, by, 1))
visited.append((rx, ry, bx, by))

def move(x, y, dx, dy):
  cnt = 0
  while board[x + dx][y + dy] != "#" and board[x][y] != "O":
    x += dx
    y += dy
    cnt += 1

  return x, y, cnt

def solve():
  while q:
    rx, ry, bx, by, depth = q.popleft()
    if depth > 10:
      break

    for i in range(4):
      nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
      nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
      if board[nbx][nby] != "O":
        if board[nrx][nry] == "O":
          print(depth)
          return
        if nrx == nbx and nry == nby:
          if rcnt > bcnt:
            nrx -= dx[i]
            nry -= dy[i]
          else:
            nbx -= dx[i]
            nby -= dy[i]

        if (nrx, nry, nbx, nby) not in visited:
          q.append((nrx, nry, nbx, nby, depth + 1))
          visited.append((nrx, nry, nbx, nby))
  print(-1)

solve()