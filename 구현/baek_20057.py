# 2022/11/04 baek 20057

import sys
input = sys.stdin.readline

N = int(input())
arr = []
before = 0

for i in range(N):
  arr.append(list(map(int, input().split())))
  before += sum(arr[i])

tornado_info = [[0, 0, 0.02, 0, 0],
                [0, 0.1, 0.07, 0.01, 0],
                [0.05, 0, 0, 0, 0],
                [0, 0.1, 0.07, 0.01, 0],
                [0, 0, 0.02, 0, 0]]

# 반시계
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def rotate(arr):
  N = len(arr)
  temp = [[0] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      temp[N - 1 - j][i] = arr[i][j]
  return temp


def spread(x, y, direction):
  center_value = arr[x][y]
  arr[x][y] = 0
  remain_value = center_value
  
  for i in range(5):
    for j in range(5):
      new_value = int(center_value * tornado_info[i][j])
      remain_value -= new_value
      if 0 <= x + (i - 2) < N and 0 <= y + (j - 2) < N:
        arr[x + (i - 2)][y + (j - 2)] += new_value

  nx = x + dx[direction]
  ny = y + dy[direction]

  if 0 <= nx < N and 0 <= ny < N:
    arr[nx][ny] += remain_value

def solution():
  global tornado_info
  x = y = N//2
  direction = 0
  move_cnt = 1
  while True:
    for i in range(2):
      for j in range(move_cnt):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if not (0 <= nx < N and 0 <= ny < N):
          result = before
          for i in range(N):
            result -= sum(arr[i])
          return result
        spread(nx, ny, direction)
        x, y = nx, ny
      # 방향 전환
      direction = (direction + 1) % 4
      tornado_info = rotate(tornado_info)
    move_cnt += 1


print(solution())