#2022/10/29 baek 14499

import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
arr = []

for _ in range(N):
  arr.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

direction_info = list(map(int, input().split()))
# 마지막 인덱스가 바닥
dice = [0, 0, 0, 0, 0, 0]

for d in direction_info:
  nx = x + dx[d - 1]
  ny = y + dy[d - 1]
  if 0 <= nx < N and 0 <= ny < M:
    if d == 1:
      dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 2:
      dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif d == 3:
      dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1] 
    elif d == 4:
      dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    
    if arr[nx][ny] == 0:
      arr[nx][ny] = dice[5]
    else:
      dice[5] = arr[nx][ny]
      arr[nx][ny] = 0

    x = nx
    y = ny
    print(dice[0])