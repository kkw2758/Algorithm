# 2022/12/13 baek 16933

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
  q = deque()
  q.append(start)
  ans = 1
  time = True
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while q:
    for _ in range(len(q)):
      x, y, w = q.popleft()

      if (x, y) == (N - 1, M - 1):
        print(ans)
        return

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] > w:
          if arr[nx][ny] == 0:
            q.append((nx, ny, w))
            visited[nx][ny] = w
          elif w < K:
            if not time:
              q.append((x, y, w))
            else:
              visited[nx][ny] = w
              q.append((nx, ny, w + 1))
    ans += 1
    time = not time
  print(-1)
  return

N, M, K = map(int, input().split())
arr = []
for _ in range(N):
  arr.append(list(map(int, list(input().rstrip()))))

visited = [[(K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0] = 0

bfs((0, 0, 0))


import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
  q = deque([start])
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  day = 1

  while q:
    night = False if day > 0 else True

    for _ in range(len(q)):
      x, y, w = q.popleft()
      today = abs(day)

      if [x, y] == [N - 1, M - 1]:
        return today

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][w]:
          if not graph[nx][ny][w]:
            visited[nx][ny][w] = today + 1
            q.append((nx, ny, w))
          elif w < K and not visited[nx][ny][w + 1]:
            if not night:
              visited[nx][ny][w + 1] = today + 1
              q.append((nx, ny, w + 1))
            else:
              q.append((x, y, w))

    day = day + 1 if day > 0 else day - 1
    day *= -1
  return -1

N, M, K = map(int, input().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0] = [1] * (K + 1)
print(bfs((0, 0, 0)))