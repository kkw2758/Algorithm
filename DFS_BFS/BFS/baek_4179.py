# 2022/10/24 Baek 4179
from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
R, C = map(int, input().split())
fire = []
arr = []
for i in range(R):
  temp = list(input())
  arr.append(temp)
  for j in range(C):
    if arr[i][j] == "J":
      start = ["J", 0, i, j]
    elif arr[i][j] == "F":
      fire.append([i,j])

visited = [[False] * C for _ in range(R)]
q = deque()
q.append(["J", 0, start[2], start[3]])
for x, y in fire:
  q.append(["F", 0, x, y])

result = -1
while q:
  symbol, t, x, y = q.popleft()
  if arr[x][y] != symbol:
    continue
  if symbol == "J" and (x == R - 1 or y == C - 1 or x == 0 or y == 0):
    result = t
    break
  visited[x][y] = True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < R and 0 <= ny < C:
      if visited[nx][ny] == False:
        if symbol == "F" and (arr[nx][ny] == "." or arr[nx][ny] == "J"):
          arr[nx][ny] = "F"
          q.append(["F", t + 1, nx, ny])
        elif symbol == "J" and arr[nx][ny] == ".":
          arr[nx][ny] = "J"
          q.append(["J", t + 1, nx, ny])

if result == -1:
  print("IMPOSSIBLE")
else:
  print(result + 1)