#2022/11/14 baek 23290

from itertools import product
from copy import deepcopy

M, S = map(int, input().split())
fish_arr = [[[] for _ in range(4)] for _ in range(4)]
smell_arr = [[0] * 4 for _ in range(4)]
for _ in range(M):
  fx, fy, d = map(int, input().split())
  fish_arr[fx - 1][fy - 1].append(d - 1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

hx = [-100, -1, 0, 1, 0]
hy = [-100, 0, -1, 0, 1]

def move_fishes():
  new_fish_arr = [[[] for _ in range(4)] for _ in range(4)]
  for x in range(4):
    for y in range(4):
      if fish_arr[x][y]:
        for d in fish_arr[x][y]:
          flag = False
          for k in range(8):
            nd = (d - k) % 8
            nx = x + dx[nd]
            ny = y + dy[nd]
            if (0 <= nx < 4 and 0 <= ny < 4) and smell_arr[nx][ny] == 0 and not(nx == sx and ny == sy):
              flag = True
              new_fish_arr[nx][ny].append(nd)
              break
          if flag == False:
            new_fish_arr[x][y].append(d)
  return new_fish_arr
          
def move_shark():
  global sx, sy
  result_list = []
  candidates = product([1,2,3,4], repeat = 3)
  for candidate in candidates:
    flag = True
    x = sx
    y = sy
    cnt = 0
    visited = set()
    for d in candidate:
      x = x + hx[d]
      y = y + hy[d]
      if 0 <= x < 4 and 0 <= y < 4:
        if fish_arr[x][y] and (x, y) not in visited:
          cnt += len(fish_arr[x][y])
          visited.add((x, y))
      else:
        flag = False
        break
    if flag == True:
      result_list.append((cnt, int("".join(list(map(str, candidate))))))

  result_list.sort(key = lambda x: (-x[0], x[1]))
  result = str(result_list[0][1])
  for d in result:
    d = int(d)
    sx = sx + hx[d]
    sy = sy + hy[d]
    if fish_arr[sx][sy]:
      fish_arr[sx][sy] = []
      smell_arr[sx][sy] = 3

def smell_down():
  for i in range(4):
    for j in range(4):
      if smell_arr[i][j] >= 1:
        smell_arr[i][j] -= 1

for i in range(S):
  temp_fish_arr = deepcopy(fish_arr)
  fish_arr = move_fishes()
  move_shark()
  smell_down()
  for i in range(4):
    for j in range(4):
      fish_arr[i][j] += temp_fish_arr[i][j]

result = 0
for i in range(4):
  for j in range(4):
    if fish_arr[i][j]:
      result += len(fish_arr[i][j])

print(result)