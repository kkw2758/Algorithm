# 2022/12/06 Baek 18809
from collections import deque
import sys
input = sys.stdin.readline

N, M, R, G = map(int, input().split())
garden = []
for _ in range(N):
  garden.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
R_start = []
G_start = []

def bfs():
  GQ = deque()
  RQ = deque()
  visited = [[-1] * M for _ in range(N)]
  for i in G_start:
    GQ.append(i)
    visited[i[0]][i[1]] = -2

  for i in R_start:
    RQ.append(i)
    visited[i[0]][i[1]] = -2

  flower = 0
  cnt = 1

  while GQ and RQ:
    for i in range(len(GQ)):
      gx, gy = GQ.popleft()
      # 꽃이 핀곳은 -100으로 나타냄
      if visited[gx][gy] == -100:
        continue
      # 초록색 배양액 퍼져 나가는 과정
      for idx in range(4):
        ngx = gx + dx[idx]
        ngy = gy + dy[idx]
        if 0 <= ngx < N and 0 <= ngy < M:
          if garden[ngx][ngy] and visited[ngx][ngy] == -1:
            visited[ngx][ngy] = cnt
            GQ.append((ngx, ngy))

    for i in range(len(RQ)):
      rx, ry = RQ.popleft()
      if visited[rx][ry] == -100:
        continue
      # 붉은색 배양액 퍼져 나가는 과정
      for idx in range(4):
        nrx = rx + dx[idx]
        nry = ry + dy[idx]
        if 0 <= nrx < N and 0 <= nry < M:
          # 호수가 아니면
          if garden[nrx][nry]:
            # 이번 회차에 초록색 배양액이 퍼졌다면 꽃을 피운다
            if visited[nrx][nry] == cnt:
              visited[nrx][nry] = -100
              flower += 1
            # 아직 초록색 배양액이 방문하지 않은곳 붉은 배양액 방문 처리
            elif visited[nrx][nry] == -1:
              # 붉은 배양액의 방문 표시를 cnt로하면 위의 과정에서 초록색 배양액의 방문 cnt로 한것과 겹침
              visited[nrx][nry] = -2
              # visited[nrx][nry] = cnt
              RQ.append((nrx, nry))
    cnt += 1

  return flower

# 백트래킹을 이용해서 주어진 배열에서 초록색 배양액, 붉은 배양액의 시작 지점의 후보를 전부 골라준다.
def dfs(R_cnt, G_cnt, start):
  global result
  if R_cnt > R or G_cnt > G:
    return
  if R_cnt == R and G_cnt == G:
    result = max(result, bfs())
    return

  for i in range(start, N * M):
    x = i // M
    y = i % M
    if garden[x][y] == 2:
      if (x, y) in R_start or (x, y) in G_start:
        continue
      else:
        G_start.append((x, y))
        dfs(R_cnt, G_cnt + 1, i + 1)
        G_start.pop()

        R_start.append((x, y))
        dfs(R_cnt + 1, G_cnt, i + 1)
        R_start.pop()

dfs(0, 0, 0)
print(result)


# combinations 모듈을 이용해서 가능한 초록색 배양액, 붉은 배양액의 시작점을 뽑는 과정
from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

def bfs(green_start, red_start):
  GQ = deque()
  RQ = deque()

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  flower = 0
  cnt = 1
  visited = [[-1] * M for _ in range(N)]

  for i in green_start:
    visited[i[0]][i[1]] = -2
    GQ.append((i[0], i[1]))
  
  for i in red_start:
    visited[i[0]][i[1]] = -2
    RQ.append((i[0], i[1]))
  
  while GQ and RQ:
    for i in range(len(GQ)):
      gx, gy = GQ.popleft()
      if visited[gx][gy] == -100:
        continue
      for idx in range(4):
        ngx = gx + dx[idx]
        ngy = gy + dy[idx]
        if 0 <= ngx < N and 0 <= ngy < M:
          if adj[ngx][ngy] and visited[ngx][ngy] == -1:
            visited[ngx][ngy] = cnt
            GQ.append((ngx, ngy))

    for i in range(len(RQ)):
      rx, ry = RQ.popleft()
      if visited[rx][ry] == -100:
        continue
      for idx in range(4):
        nrx = rx + dx[idx]
        nry = ry + dy[idx]
        if 0 <= nrx < N and 0 <= nry < M:
          if adj[nrx][nry]:
            if visited[nrx][nry] == cnt:
              visited[nrx][nry] = -100
              flower += 1
            elif visited[nrx][nry] == -1:
              visited[nrx][nry] = -2
              RQ.append((nrx, nry))
    cnt += 1

  return flower

N, M, G, R = map(int, input().split())
adj = [list(map(int, input().split())) for _ in range(N)]
result = 0
# 처음에 배양액을 놓을 수 있는 좌표들
can_start = []

for i in range(N):
  for j in range(M):
    if adj[i][j] == 2:
      can_start.append((i, j))

for red_green_start in combinations(can_start, R+G):
  for green_start in combinations(red_green_start, G):
    red_start = [x for x in red_green_start if x not in green_start]
    result = max(result, bfs(green_start, red_start))

print(result)


# 다른풀이
from itertools import combinations
from collections import deque

N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]
grounds = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
  for j in range(M):
    if garden[i][j] == 2:
      grounds.append((i, j))

def bfs(gl, rl):
  visit = [[0] * M for _ in range(N)]
  cnt = 0
  q = deque()
  for g in gl:
    q.append((g[0], g[1], 'g'))
    visit[g[0]][g[1]] = -1
  for r in rl:
    q.append((r[0], r[1], 'r'))
    visit[r[0]][r[1]] = 1

  while q:
    x, y, color = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and garden[nx][ny] != 0 and visit[nx][ny] == 0:
        # 초록
        if visit[x][y] < 0:
          visit[nx][ny] = visit[x][y] - 1
          q.append((nx, ny, color))
        elif 0 < visit[x][y] < 999999:
          visit[nx][ny] = visit[x][y] + 1
          q.append((nx, ny, color))

      if 0 <= nx < N and 0 <= ny < M and garden[nx][ny] != 0 and abs(visit[x][y] + visit[nx][ny]) == 1:
        visit[nx][ny] = 999999
        cnt += 1
  return cnt

gs = set(grounds)
res = 0
for green in combinations(grounds, G):
  groundSetMinusGreen = list(gs - set(green))
  green_list = list(green)
  for red in combinations(groundSetMinusGreen, R):
    red_list = list(red)
    result = bfs(green_list, red_list)
    if res < result:
      res = result

print(res)