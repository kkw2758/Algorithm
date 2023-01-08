#2022/11/12 baek 20056

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
fire_balls = []
for _ in range(M):
  r, c, m, s, d = list(map(int, input().split()))
  fire_balls.append([r - 1, c - 1, m, s, d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(K):
  temp = [[[] for _ in range(N)] for _ in range(N)]
  for fire_ball in fire_balls:
    r, c, m, s, d = fire_ball
    nr = (r + dx[d] * s) % N
    nc = (c + dy[d] * s) % N
    temp[nr][nc].append([m, s, d])

  fire_balls = []
  for row in range(N):
    for col in range(N):
      fire_ball_cnt = len(temp[row][col])
      if fire_ball_cnt >= 2:
        odd = 0
        even = 0
        new_m = 0
        new_s = 0

        for idx in range(fire_ball_cnt):
          new_m += temp[row][col][idx][0]
          new_s += temp[row][col][idx][1]
          if temp[row][col][idx][2] % 2 == 0:
            even += 1
          else:
            odd += 1

        new_m = new_m // 5
        new_s = new_s // fire_ball_cnt

        if new_m == 0:
          continue
        if even * odd == 0:
          for new_d in [0,2,4,6]:
            fire_balls.append([row, col, new_m, new_s, new_d])
        else:
          for new_d in [1,3,5,7]:
            fire_balls.append([row, col, new_m, new_s, new_d])

      elif fire_ball_cnt == 1:
        fire_balls.append((row, col, temp[row][col][0][0], temp[row][col][0][1], temp[row][col][0][2]))

total_m = 0
for fire_ball in fire_balls:
  total_m += fire_ball[2]

print(total_m)