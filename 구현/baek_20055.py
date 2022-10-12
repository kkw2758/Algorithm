#2022/10/12 baek_20055

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ary = list(map(int, input().split()))
robot = [False] * n

cnt = 0
while True:
  last = ary.pop()
  ary = [last] + ary
  robot.pop()
  robot = [False] + robot
  robot[-1] = False

  for i in range(n - 1, 0, -1):
      if not robot[i] and robot[i - 1] and ary[i] > 0:
        ary[i] -= 1
        robot[i] = True
        robot[i - 1] = False

  robot[-1] = False

  if ary[0] != 0 and not robot[0]:
    ary[0] -= 1
    robot[0] = True

  zero_cnt = 0
  for i in range(2 * n):
    if ary[i] == 0:
      zero_cnt += 1

  cnt += 1

  if zero_cnt >= k:
    break

print(cnt)

# import sys
# from collections import deque
# input = sys.stdin.readline

# n, k = map(int, input().split())

# ary = deque(map(int, input().split()))
# robot = deque([False] * n)

# cnt = 0
# while True:
#   robot.rotate(1)
#   ary.rotate(1)
#   robot[-1] = False

#   for i in range(n - 1, 0, -1):
#       if not robot[i] and robot[i - 1] and ary[i] > 0:
#         ary[i] -= 1
#         robot[i] = True
#         robot[i - 1] = False

#   robot[-1] = False

#   if ary[0] > 0 and not robot[0]:
#     ary[0] -= 1
#     robot[0] = True

#   zero_cnt = 0
#   for i in range(2 * n):
#     if ary[i] == 0:
#       zero_cnt += 1
#   cnt += 1
#   if zero_cnt >= k:
#     break

# print(cnt)