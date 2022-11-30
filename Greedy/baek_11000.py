# 2022/11/30 Baek 11000

import heapq
import sys

input = sys.stdin.readline

N = int(input())
courses = []
for _ in range(N):
  courses.append(list(map(int, input().split())))

courses.sort()

room = []
heapq.heappush(room, courses[0][1])
for i in range(1, N):
  if room[0] <= courses[i][0]:
    heapq.heappop(room)
    heapq.heappush(room, courses[i][1])
  else:
    heapq.heappush(room, courses[i][1])

print(len(room))