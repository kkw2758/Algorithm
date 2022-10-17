#2022/10/17 baek 14891

from collections import deque

def rotate_wheel(wheel_number, direction):
  rotate_info = [[wheel_number - 1, direction]]
  left_before = wheel_number - 1
  right_before = wheel_number - 1

  # 왼쪽
  before = direction
  for left_now in range(wheel_number - 2, -1, -1):
    print("left 통과", left_now, left_before)
    if wheels[left_before][-2] != wheels[left_now][2]:
      if before == -1:
        rotate_info.append([left_now, 1])
        before = 1
      elif before == 1:
        rotate_info.append([left_now, -1])
        before = -1
      left_before = left_now
    else:
      print("left 끝", left_now, left_before)
      break

  # 오른쪽
  before = direction
  for right_now in range(wheel_number, 4):
    if wheels[right_before][2] != wheels[right_now][-2]:
      if before == -1:
        rotate_info.append([right_now, 1])
        print("right", right_now)
        before = 1
      elif before == 1:
        rotate_info.append([right_now, -1])
        print("right", right_now)
        before = -1
      right_before = right_now
    else:
      break
  
  print(rotate_info)
  for wheel_number, direction in rotate_info:
    wheels[wheel_number].rotate(direction)

wheels = []

for i in range(4):
  wheels.append(deque(list(input())))

k = int(input())
for _ in range(k):
  # 회전하는 톱니 번호, 시계 0 / 반시계 -1
  for _ in wheels:
    print(_)
  print()
  wheel_number, direction = map(int, input().split())
  rotate_wheel(wheel_number, direction)

for _ in wheels:
  print(_)

result = 0
for i in range(4):
  if wheels[i][0] == "1":
    result += 2 ** i

print(result)

# 재귀를 이용한 풀이
import sys
from collections import deque

def check_right(start, dirs):
  if start > 4 or gears[start - 1][2] == gears[start][6]:
    return

  if gears[start - 1][2] != gears[start][6]:
    check_right(start + 1, - dirs)
    gears[start].rotate(dirs)


def check_left(start, dirs):
  if start < 1 or gears[start][2] == gears[start + 1][6]:
    return

  if gears[start + 1][6] != gears[start][2]:
    check_left(start - 1, -dirs)
    gears[start].rotate(dirs)


gears = {}
for i in range(1, 5):
  gears[i] = deque(list(map(int, list(input()))))

k = int(input())
for _ in range(k):
  num, dirs = map(int, input().split())

  check_right(num + 1, - dirs)
  check_left(num - 1, - dirs)
  gears[num].rotate(dirs)

result = 0
for i in range(4):
  result += (2 ** i) * gears[i + 1][0]
print(result)