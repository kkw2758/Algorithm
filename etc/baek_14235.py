# 2023/03/31 Baek 14235

import sys
import heapq
input = sys.stdin.readline

n = int(input())

presents = []
for _ in range(n):
    new_presents = list(map(int, input().split()))
    for new_present in new_presents[1:]:
        heapq.heappush(presents, -new_present)
    if new_presents[0] == 0:
      if presents:
        print("result",-heapq.heappop(presents))
      else:
        print("result",-1)