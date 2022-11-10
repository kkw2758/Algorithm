# 2022/11/10 Baek 17142

# 비활성 상태인 바이러스는 타고 넘어거서 이동할 수 있다. (벽이 아니기 때문)
# 모든 칸에 바이러스가 퍼지는 최소 시간을 구할 때, 활성 상태 바이러스가 비활성 상태인 바이러스 자리까지
# 도달 하는 데에 걸리는 시간은 고려하지 않는다.

from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
virus_index = []


for i in range(N):
  arr.append(list(map(int, input().split())))
  for j in range(N):
    if arr[i][j] == 2:
      virus_index.append((i, j))

def is_full():
  for i in range(N):
    for j in range(N):
      if visited[i][j] == False and arr[i][j] != 1:
        return False

  return True

def bfs(candidate):
  max_cnt = 0
  q = deque()
  for i, j in candidate:
    q.append((i, j, 0))
    visited[i][j] = True

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]
  while q:
    x, y, cnt = q.popleft()
    if (x, y) not in virus_index:
      max_cnt = max(max_cnt, cnt)
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        # 벽이 아니고 방문을 안했을때
        if arr[nx][ny] != 1 and visited[nx][ny] == False:
          visited[nx][ny] = True
          q.append((nx, ny, cnt + 1))

  return max_cnt

result = int(1e9)
candidates = list(combinations(virus_index, M))
for candidate in candidates:
  visited = [[False] * N for _ in range(N)]
  cnt = bfs(candidate)
  flag = is_full()
  if flag == True:
    result = min(result, cnt)

if result == int(1e9):
  print(-1)
else:
  print(result)


# 다른 풀이
from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(active):
  q = deque()
  visited = [[-1] * n for _ in range(n)]
  result = 0

  for x, y in active:
    q.append((x, y))
    visited[x][y] = 0

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 0 and visited[nx][ny] == -1:
          q.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1
          result = max(result, visited[nx][ny])
        elif graph[nx][ny] == 2 and visited[nx][ny] == -1:
          q.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1

  if list(sum(visited, [])).count(-1) != wall_cnt:
    return inf
  return result

wall_cnt = 0
virus = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      wall_cnt += 1
    elif graph[i][j] == 2:
      virus.append((i,j))

ans = inf
for active in combinations(virus, m):
  ans = min(ans, bfs(active))

print(ans if ans != inf else -1)