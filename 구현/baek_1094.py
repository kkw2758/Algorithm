# 2023/02/06 Baek 1094

import heapq
X = float(input())
sticks = [64]

while sum(sticks) != X:
  now = heapq.heappop(sticks)
  if sum(sticks) + now/2 >= X:
    heapq.heappush(sticks,now/2)
  else:
    heapq.heappush(sticks,now/2)
    heapq.heappush(sticks,now/2)

print(len(sticks))