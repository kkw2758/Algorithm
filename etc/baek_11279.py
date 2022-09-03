# 2022/09/04 Baek 11279

import sys, heapq

q = []
input = sys.stdin.readline
N = int(input())
for _ in range(N):
  x = int(input())
  if x == 0:
    if len(q) == 0:
      print("out", 0)
    else:
      print("out", -heapq.heappop(q))
  else:
    heapq.heappush(q, -x)