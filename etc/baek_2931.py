# 2023/01/09 Baek 2931
# 참고 사이트 : https://chldkato.tistory.com/69
# 풀다가 87%에서 계속 오류가 나서 위 사이트를 참고 하였음.
# M과 Z각각에서 bfs 실행하여 파이프를 추가하여야 하는 좌료를 px, py로 잡고 필요한 방향을 check_list 리스트에 담는다

from collections import deque
import sys

input = sys.stdin.readline
# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def direction(s):
  if s == "|":
    return [1, 3]
  elif s == "-":
    return [0, 2]
  elif s == "+" or s == "M" or s == "Z":
    return [0, 1, 2, 3]
  elif s == "1":
    return [0, 1]
  elif s == "2":
    return [0, 3]
  elif s == "3":
    return [2, 3]
  elif s == "4":
    return [1, 2]

def bfs(x, y, dir):
  global px, py
  q = deque()
  q.append([x, y, dir])
  visited[x][y] = 1
  while q:
    x, y, dir = q.popleft()
    for d in dir:
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
        if board[nx][ny] != ".":
          visited[nx][ny] = 1
          ndir = direction(board[nx][ny])
          q.append([nx, ny, ndir])
        else:
          if board[x][y] == "M" or board[x][y] == "Z":
            continue
          if not px and not py:
            px, py = nx + 1, ny + 1
          nd = (d + 2) % 4
          if nd not in check_list:
            check_list.append(nd)

M, N = map(int, input().split())
visited = [[0] * N for _ in range(M)]

board = []
for i in range(M):
  row = list(input().strip())
  board.append(row)
  for j in range(N):
    if row[j] == "M":
      sx, sy = i, j
    elif row[j] == "Z":
      zx, zy = i, j

check_list, px, py = [], 0, 0
bfs(sx, sy, [0, 1, 2, 3])
bfs(zx, zy, [0, 1, 2, 3])

for i in range(M):
  for j in range(N):
    if board[i][j] != "." and not visited[i][j]:
      bfs(i, j, direction(board[i][j]))

check_list.sort()

if len(check_list) == 4:
  print(px, py, "+")
else:
  block_list = ["|", "-", "1", "2", "3", "4"]
  for s in block_list:
    if check_list == direction(s):
      print(px, py, s)