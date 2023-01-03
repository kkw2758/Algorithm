# 2023/01/03 Baek 20304

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
P = list(map(int, input().split()))
visited = [-1 for _ in range(N + 1)]
q = deque()

for i in P:
  visited[i] = 0
  q.append(i)

while q:
  now = q.popleft()
  for i in range(20):
    next = (1 >> i) ^ now
    if next <= N and visited[next] == -1:
      visited[next] = visited[now] + 1
      q.append(next)

if N:
  print(max(visited))
else:
  print(0)