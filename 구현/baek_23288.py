#2022/10/23 baek 23288

from collections import deque

def bfs(x, y):
  cnt = 0
  start_point = arr[x][y]
  visited = [[False] * m for _ in range(n)]
  visited[x][y] = True
  q = deque()
  q.append([x, y])
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
        if arr[nx][ny] == start_point:
          visited[nx][ny] = True
          q.append([nx, ny])
          cnt += 1

  return cnt

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))
dice = [1, 2, 3, 4, 5, 6]

dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

direction, result, x, y = 0, 0, 0, 0

for i in range(k):
  if not(0 <= x + dx[direction] < n and 0 <= y + dy[direction] < m):
    direction = (direction + 2) % 4
  
  if direction == 0:
    dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
  elif direction == 1:
    dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
  elif direction == 2:
    dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
  else:
    dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

  x, y = x + dx[direction], y + dy[direction]
  result += arr[x][y] * (bfs(x, y) + 1)
  A = dice[-1]
  B = arr[x][y]
  if A > B:
    direction = (direction + 1) % 4
  elif A < B:
    direction = (direction - 1) % 4

print(result)