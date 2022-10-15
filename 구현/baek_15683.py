# 2022/10/15 baek 15683

from itertools import product
from copy import deepcopy
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

camera_direction = [
  [],
  [0, 1, 0, 0],
  [0, 1, 0, 1],
  [1, 1, 0, 0],
  [1, 1, 0, 1],
  [1, 1, 1, 1]
]

n, m = map(int, input().split())
arr = []
cameras = []


for i in range(n):
  temp = list(map(int, input().split()))
  arr.append(temp)
  for j in range(len(temp)):
    if 0 < temp[j] < 6:
      cameras.append((temp[j], i, j))

# 카메라 돌리는정도
candidates = list(product([0,1,2,3], repeat = len(cameras)))

def rotate(arr, n):
  return arr[n:] + arr[:n]

result = 64


for candidate in candidates:
  # print(candidate)
  tmp_arr = deepcopy(arr)
  for idx in range(len(cameras)):
    camera_number, x, y = cameras[idx]
    direction = camera_direction[camera_number]
    direction = rotate(direction, candidate[idx])
    for i in range(4):
      if direction[i] == 0:
        continue
      else:
        for j in range(8):
          nx = x + dx[i] * (j + 1)
          ny = y + dy[i] * (j + 1)
          if 0 <= nx < n and 0 <= ny < m:
            if tmp_arr[nx][ny] == 6:
              break
            elif tmp_arr[nx][ny] == 0:
              tmp_arr[nx][ny] = "#"
          
  cnt = 0
  for i in range(n):
    for j in range(m):
      if tmp_arr[i][j] == 0:
        cnt += 1

  result = min(result, cnt)

print(result)

# DFS를 이용한 풀이
import copy

n, m = map(int, input().split())
cctv = []
graph = []
mode = [
  [],
  [[0], [1], [2], [3]],
  [[0, 2], [1, 3]],
  [[0, 1], [1, 2], [2, 3], [3, 0]],
  [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
  [[0, 1, 2, 3]]
]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
  data = list(map(int, input().split()))
  graph.append(data)
  for j in range(m):
    if data[j] in [1, 2, 3, 4, 5]:
      cctv.append([data[j], i, j])

def fill(board, directions, x, y):
  for i in directions:
    nx = x
    ny = y
    while True:
      nx += dx[i]
      ny += dy[i]
      if not(0 <= nx < n and 0 <= ny < m):
        break
      if board[nx][ny] == 6:
        break
      elif board[nx][ny] == 0:
        board[nx][ny] = 7

def dfs(depth, arr):
  global min_value
  if depth == len(cctv):
    count = 0
    for i in range(n):
      for j in range(m):
        if arr[i][j] == 0:
          count += 1
    min_value = min(min_value, count)
    return
  temp = copy.deepcopy(arr)
  cctv_num, x, y = cctv[depth]
  for i in mode[cctv_num]:
    fill(temp, i, x, y)
    dfs(depth + 1, temp)
    temp = copy.deepcopy(arr)

min_value  = int(1e9)
dfs(0, graph)
print(min_value)