# 2022/09/04 Baek 11279

import sys, heapq

q = []
input = sys.stdin.readline
N = int(input())
for _ in range(N):
  x = int(input())
  if x == 0:
    if len(q) == 0:
      print(0)
    else:
      print(-heapq.heappop(q))
  else:
    heapq.heappush(q, -x)