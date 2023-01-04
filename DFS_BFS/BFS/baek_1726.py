# 2023/01/03 Baek 1726


from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

def bfs():
  q = deque()
  q.append([startX - 1, startY - 1, startD, 0])
  visit = [[[0 for i in range(5)] for i in range(n)] for i in range(m)]
  visit[startX - 1][startY - 1][startD] = 1

  while q:
    x, y, d, cnt = q.popleft()
    if (x, y, d) == (endX - 1, endY - 1, endD):
      return cnt
    nx = x
    ny = y
    for i in range(3):
      nx += dx[d]
      ny += dy[d]
      if 0 <= nx < m and 0 <= ny < n and visit[nx][ny][d] == 1:
        continue
      if 0 <= nx < m and 0 <= ny < n and s[nx][ny] != 1:
        visit[nx][ny][d] = 1
        q.append([nx, ny, d, cnt + 1])
      else:
        break

    for i in range(1, 5):
      if d != i and visit[x][y][i] == 0:
        visit[x][y][i] = 1
        if (d == 1 and i == 2) or (d == 2 and i == 1) or (d == 3 and i == 4) or (d == 4 and i == 3):
          q.append([x, y, i, cnt + 2])
        else:
          q.append([x, y, i, cnt + 1])

m, n = map(int, input().split())
s = [list(map(int, input().split())) for i in range(m)]
startX, startY, startD = map(int, input().split())
endX, endY, endD = map(int, input().split())
print(bfs())


import sys
input = sys.stdin.readline
from collections import deque

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
change_dir = [[2, 3], [2, 3], [0, 1], [0, 1]]

def bfs():
  visited = [[[0] * 4 for _ in range(C)] for _ in range(R)]
  visited[sr - 1][sc - 1][sd - 1] = 1
  q = deque()
  q.append((sr - 1, sc - 1, sd - 1, 0))
  
  while q:
    r, c, d, cnt = q.popleft()
    if (r, c, d) == (er - 1, ec - 1, ed - 1):
      return cnt

    for dis in range(1, 4):
      nr = r + dr[d] * dis
      nc = c + dc[d] * dis
      
      if not(0 <= nr < R and 0 <= nc < C) or A[nr][nc]:
        break
      if visited[nr][nc][d]:
        continue
      q.append((nr, nc, d, cnt + 1))
      visited[nr][nc][d] = 1

    for nd in change_dir[d]:
      if visited[r][c][nd]:
        continue
      q.append((r, c, nd, cnt + 1))
      visited[r][c][nd] = 1

R, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
sr, sc, sd = map(int, input().split())
er, ec, ed = map(int, input().split())

print(bfs())