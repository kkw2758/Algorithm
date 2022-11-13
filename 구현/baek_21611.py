#2022/11/13 baek 21611
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
blizards = []
for _ in range(M):
  d, s = map(int, input().split())
  blizards.append([d, s])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

center = (N//2, N//2)

def blizard(d, s):
  x, y = center
  for i in range(1, s + 1):
    nx = x + dx[d] * i
    ny = y + dy[d] * i
    arr[nx][ny] = 0

def move_balls():
  x, y = center
  balls = []
  for i in range(1, N + 1):
    if i % 2 == 1:
      d_info = [2, 1]
    else:
      d_info = [3, 0]

    for d in d_info:
      for _ in range(i):
        x = x + dx[d]
        y = y + dy[d]
        if not(0 <= x < N and 0 <= y < N):
          return balls
        if arr[x][y] != 0:
          balls.append(arr[x][y])

def break_balls(balls):
  score = 0
  temp = []
  cnt = 1
  if balls:
    before = balls[0]
    for ball in balls[1:]:
      if before == ball:
        cnt += 1
      else:
        if 0 < cnt < 4:
          temp += [before] * cnt
        elif cnt >= 4:
          score += before * cnt 
        cnt = 1
        before = ball

    if 0 < cnt < 4:
      temp += [before] * cnt
    elif cnt >= 4:
      score += before * cnt

  return temp, score

def change_balls(balls):
  new_balls = []
  if balls:
    cnt = 1
    before = balls[0]
    for ball in balls[1:]:
      if before == ball:
        cnt += 1
      else:
        A = cnt
        B = before
        new_balls += [A, B]
        cnt = 1
        before = ball

    A = cnt
    B = before
    new_balls += [A, B]

  return new_balls

def convert_2_to_1(balls):
  new_arr = [[0] * N for _ in range(N)]
  x, y = center
  for i in range(1, N + 1):
    if i % 2 == 1:
      d_info = [2, 1]
    else:
      d_info = [3, 0]

    for d in d_info:
      for _ in range(i):
        x = x + dx[d]
        y = y + dy[d]

        if not(0 <= x < N and 0 <= y < N) or not(balls):
          return new_arr
        else:
          new_arr[x][y] = balls.pop(0)

  return new_arr


total_score = 0
for d, s in blizards:
  blizard(d - 1, s)
  balls = move_balls()
  # print(balls)
  while True:
    balls, score = break_balls(balls)
    if score == 0:
      break
    total_score += score
  # print(balls)
  balls = change_balls(balls)
  # print(balls)

  arr = convert_2_to_1(balls)
  # for _ in arr:
  #   print(_)

print(total_score)