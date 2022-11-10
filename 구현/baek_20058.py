# 2022/11/09 baek 20058
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = []
for _ in range(2 ** N):
  arr.append(list(map(int, input().split())))

L_list = list(map(int, input().split()))

visited = [[False] * (2 ** N) for _ in range(2 ** N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def rotate_90(arr):
  n = len(arr)
  temp = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      temp[j][n - i - 1] = arr[i][j]
  return temp

def fire_storm(L):
  for i in range(0, 2 ** N, 2 ** L):
    for j in range(0, 2 ** N, 2 ** L):
      temp = [[0] * (2 ** L) for _ in range(2 ** L)]
      for row in range(2 ** L):
        for col in range(2 ** L):
          temp[row][col] = arr[i + row][j + col]
      
      temp = rotate_90(temp)
      for row in range(2 ** L):
        for col in range(2 ** L):
          arr[i + row][j + col] = temp[row][col]
  
  temp = [[0] * (2 ** N) for _ in range(2 ** N)]

  for x in range(2 ** N):
    for y in range(2 ** N):
      if arr[x][y] >= 1:
        cnt = 0
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N:
            if arr[nx][ny] != 0:
              cnt += 1
        if cnt < 3:
          temp[x][y] = -1

  for x in range(2 ** N):
    for y in range(2 ** N):
      if temp[x][y] == -1:
        arr[x][y] -= 1

def dfs(x, y):
  stack = [(x, y)]
  visited[x][y] = True
  cnt = 1
  while stack:
    x, y = stack.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N and visited[nx][ny] == False:
        if arr[nx][ny] != 0:
          stack.append((nx, ny))
          visited[nx][ny] = True
          cnt += 1

  return cnt

for i in range(Q):
  fire_storm(L_list[i])

total_ice = 0
biggest_ice = 0
for i in range(2 ** N):
  for j in range(2 ** N):
    total_ice += arr[i][j]
    if arr[i][j] != 0 and visited[i][j] == False:
      biggest_ice = max(biggest_ice, dfs(i,j))

print(total_ice)
print(biggest_ice)
