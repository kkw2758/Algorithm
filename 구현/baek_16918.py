# 2022/10/30 baek 16918
import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
arr = []
bomb = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(R):
  temp = list(input())
  arr.append(temp)
  for j in range(C):
    if arr[i][j] == "O":
      bomb.append((i, j))

for t in range(2, N + 1):
  if t % 2 == 0:
    for i in range(R):
      for j in range(C):
        if arr[i][j] != "O":
          arr[i][j] = "O"
  else:
    for x, y in bomb:
      arr[x][y] = "."
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
          arr[nx][ny] = "."
    bomb = []
    for i in range(R):
      for j in range(C):
        if arr[i][j] == "O":
          bomb.append((i,j))

for i in range(R):
  for j in range(C):
    print(arr[i][j], end = "")
  print()
