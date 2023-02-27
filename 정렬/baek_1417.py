# 2023/02/27 Baek 1417
import heapq
import sys
input = sys.stdin.readline

N = int(input())
candidates = []
result = 0
for i in range(N):
    if i == 0:
        dasom = int(input())
        continue
    heapq.heappush(candidates, int(input()) * -1)
  
if N == 1:
    print(0)
else:
  while True:
      # print(heapq.heappop(candidates))
      if dasom > candidates[0] * -1:
          print(result)
          break
      result += 1
      dasom += 1
      heapq.heappush(candidates, heapq.heappop(candidates) + 1)