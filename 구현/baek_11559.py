# 2022/10/28 Baek 11559

arr = []
for _ in range(12):
  arr.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[0] * 6 for _ in range(12)]

from collections import deque

def check(x, y):
  for i in range(x - 1, -1, -1):
    if arr[i][y] != ".":
      return i
  return -1

def reload():
  for i in range(11, -1, -1):
    for j in range(5, -1, -1):
      if arr[i][j] == ".":
        index = check(i, j)
        if index != -1:
          for k in range(index, -1, -1):
            arr[k - index + i][j] = arr[k][j]
            arr[k][j] = "."

def bfs(x, y):
  global flag
  visited = set()
  visited.add((x, y))
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < 12 and 0 <= ny < 6:
        if (nx, ny) not in visited and arr[x][y] == arr[nx][ny]:
          visited.add((nx, ny))
          q.append((nx, ny))

  visited = list(visited)
  if len(visited) >= 4:
    for x, y in visited:
      arr[x][y] = "."
    flag = True
    return True

  return False

cnt = 0
while True:
  flag = False
  for i in range(12):
    for j in range(6):
      if arr[i][j] != ".":
        bfs(i,j)

  if flag:
    cnt += 1
    reload()
  else:
    break

print(cnt)