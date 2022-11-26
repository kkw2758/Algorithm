# 2022/11/26 Baek 2217

import sys
input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
  ropes.append(int(input()))

ropes.sort()

result = 0
for i in range(len(ropes)):
  result = max(result, (N - i) * ropes[i])

print(result)