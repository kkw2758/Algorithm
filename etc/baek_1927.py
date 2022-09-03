# 2022/09/03 Baek 1927

import heapq
import sys

input = sys.stdin.readline
N = int(input())

q = []
for _ in range(N):
  x = int(input())
  if x == 0:
    if len(q) == 0:
      print("out", 0)
    else:
      print("out",heapq.heappop(q))
  else:
    heapq.heappush(q, x)