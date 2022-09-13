# 2022/09/13 Baek 11725

# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)
  
visited = [0] * (N + 1)

def dfs(start):
  for i in graph[start]:
    if visited[i] == 0:
      visited[i] = start
      dfs(i)

dfs(1)

for x in range(2, N + 1):
  print(visited[x])

# BFS
import sys
from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)
  
visited = [0] * (N + 1)

def bfs(start):
  queue = deque()
  queue.append(start)
  while queue:
    now = queue.popleft()
    for next_node in graph[now]:
      if visited[next_node] == 0:
        visited[next_node] = now
        queue.append(next_node)

bfs(1)
for x in range(2, N + 1):
  print(visited[x])