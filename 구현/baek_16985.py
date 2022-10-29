# 2022/10/29 baek 16985

from collections import deque
from itertools import permutations

INF = int(1e9)
result = INF
maze = []
for _ in range(5):
  temp = []
  for i in range(5):
    temp.append(list(map(int, input().split())))
  maze.append(temp)

temp_maze = [[[0] * 5 for _ in range(5)] for _ in range(5)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def rotate_90(arr):
  result_matrix = [[0] * 5 for _ in range(5)]
  for i in range(5):
    for j in range(5):
      result_matrix[j][4 - i] = arr[i][j]

  return result_matrix

def bfs():
  global result
  visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
  q = deque()
  q.append((0, 0, 0))

  while q:
    x, y, z = q.popleft()
    if x == 4 and y == 4 and z == 4:
      result = min(result, visited[4][4][4])
      if result == 12:
        print(result)
        exit()
      return
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5:
        if visited[nx][ny][nz] == 0 and temp_maze[nx][ny][nz] == 1:
          q.append((nx, ny, nz))
          visited[nx][ny][nz] = visited[x][y][z] + 1

def dfs(layer):
  if layer == 5:
    if temp_maze[4][4][4]:
      bfs()
    return

  for _ in range(4):
    if temp_maze[0][0][0]:
      dfs(layer + 1)
    temp_maze[layer] = rotate_90(temp_maze[layer])


def solve():
  for d in permutations([0, 1, 2, 3, 4]):
    for i in range(5):
      temp_maze[d[i]] = maze[i]
    dfs(0)

solve()

if result == INF:
  result = -1

print(result)