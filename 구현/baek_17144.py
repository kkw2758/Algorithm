# 2022/11/02 baek 17144

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = []
for i in range(R):
  arr.append(list(map(int, input().split())))

for i in range(R):
  if arr[i][0] == -1:
    up = i
    down = i + 1
    break 

dx = [-1, 0, 1, 0]
dy = [0, -1, 0 ,1]

def get_dust_list():
  result = []
  for i in range(R):
    for j in range(C):
      if arr[i][j] > 0:
        result.append((i, j, arr[i][j]))

  return result

def spread():
  dust_list = get_dust_list()
  for x, y, value in dust_list:
    cnt = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
        arr[nx][ny] += value // 5
        cnt += 1
    arr[x][y] -= (value // 5) * cnt

def up_circulate():
  dx = [0, -1, 0, 1]
  dy = [1, 0, -1, 0]
  before = 0
  direct = 0
  x, y = up, 1
  while True:
    if x == up and y == 0:
      break
    nx = x + dx[direct]
    ny = y + dy[direct]
    if not(0 <= nx < R and 0 <= ny < C):
      direct += 1
      continue
    arr[x][y], before = before, arr[x][y]
    x = nx
    y = ny

def down_circulate():
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  before = 0
  direct = 0
  x, y = down, 1
  while True:
    if x == down and y == 0:
      break
    nx = x + dx[direct]
    ny = y + dy[direct]
    if not(0 <= nx < R and 0 <= ny < C):
      direct += 1
      continue
    arr[x][y], before = before, arr[x][y]
    x = nx
    y = ny

for _ in range(T):
  spread()
  up_circulate()
  down_circulate()

answer = 0
for i in range(R):
  for j in range(C):
    if arr[i][j] > 0:
      answer += arr[i][j]

print(answer)



import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

up = -1
down = -1
# 공기 청정기 위치 찾기
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지 확산
def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        tmp_arr[nx][ny] += arr[i][j] // 5
                        tmp += arr[i][j] // 5
                arr[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp_arr[i][j]

# 공기청정기 위쪽 이동
def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x = nx
        y = ny


for _ in range(t):
    spread()
    air_up()
    air_down()

answer = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            answer += arr[i][j]

print(answer)