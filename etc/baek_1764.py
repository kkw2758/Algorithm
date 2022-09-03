# 2022/09/03 Baek 1764

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
listen = set()
see = set()
for _ in range(N):
  listen.add(input())
for _ in range(M):
  see.add(input())

result = list(listen & see)
result.sort()
print(len(result))
for i in result:
  print(i, end ="")