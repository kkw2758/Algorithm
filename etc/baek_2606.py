# 2022/09/03 Baek 2606

from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (N + 1)

def bfs(start):
  queue = deque()
  queue.append(start)
  visited[start] = True

  while queue:
    node = queue.popleft()
    for i in graph[node]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

  result = 0
  for idx in range(2, len(visited)):
    if visited[idx]:
      result += 1
  return result

print(bfs(1))


N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (N + 1)

def dfs(start):
  stack = [start]
  visited = [False] * (N + 1)

  while stack:
    node = stack.pop()
    for i in graph[node]:
      if not(visited[i]):
        stack.append(i)
        visited[i] = True

    result = 0
    for idx in range(2, len(visited)):
      if visited[idx]:
        result += 1

  return result

print(dfs(1))