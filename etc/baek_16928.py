# 2022/09/11 Baek 16928

from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
visited = [False] * 101
dist = [0] * 101
ladder_snake = {}
for _ in range(N + M):
  x, y = map(int, input().split())
  ladder_snake[x] = y

def bfs():
  q = deque()
  q.append(1)
  visited[1] = True
  while q:
    x = q.popleft()
    for i in range(1, 7):
      next = x + i
      if 1 <= next <= 100:
        if next in ladder_snake:
          next = ladder_snake[next]
        if not visited[next]:
          q.append(next)
          visited[next] = True
          dist[next] = dist[x] + 1

bfs()
print(dist[100])