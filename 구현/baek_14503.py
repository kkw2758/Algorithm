#2022/10/18 baek 14503

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

# d 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arr = []

for _ in range(n):
  arr.append(list(map(int, input().split())))

def clean(x, y, d):
  cnt = 1
  arr[x][y] = 2
  while True:
    flag = False
    for i in range(1, 5):
      nx = x + dx[(d - i) % 4]
      ny = y + dy[(d - i) % 4]
      if arr[nx][ny] == 0:
        arr[nx][ny] = 2
        d = (d - i) % 4
        x = nx
        y = ny
        flag = True
        cnt += 1
        break
    # 후진
    if flag == False:
      x = x - dx[d]
      y = y - dy[d]
      if arr[x][y] == 1:
        return cnt


print(clean(r,c,d))