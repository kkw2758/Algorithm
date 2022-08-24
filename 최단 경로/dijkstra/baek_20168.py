import heapq
from this import d

def dijkstra(start):
  global result
  h = []
  heapq.heappush(h, [0, 0, start])
  while h:
    max_cost, total_cost, now = heapq.heappop(h)
    if total_cost > c:
      continue
    for x in graph[now]:
      cost = total_cost + x[1]
      if cost > c or visited[now][x[0]]:
        continue
      elif x[0] == b:
        result = min(result, max(max_cost, x[1]))
      visited[now][x[0]] = True
      heapq.heappush(h, [max(max_cost, x[1]), cost, x[0]])

INF = int(1e9)
n, m ,a, b, c = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  start, end, cost = map(int, input().split())
  graph[start].append((end, cost))
  graph[end].append((start, cost))

result = INF
visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]

dijkstra(a)

if result != INF:
  print(result)
else:
  print(-1)



import sys

n, m, a, b, c = map(int, input().split())

board = [[] for _ in range(n + 1)]
visited = [[False] for _ in range(n + 1)]
answer = sys.maxsize

def dfs(start, end, cost, maxShame):
  visited[start] = True
  global answer
  if start == end:
    answer = min(answer, maxShame)
    return
  for item in board[start]:
    nextNode = item[0]
    nextCost = item[1]
    if visited[nextNode] == True:
      continue
    if nextCost > cost:
      continue
    visited[nextNode] = True
    dfs(nextNode, end, cost - nextCost, max(maxShame, nextCost))
    visited[nextNode] = False

for _ in range(m):
  n1, n2, cost = map(int, input().split())
  board[n1].append((n2, cost))
  board[n2].append((n1, cost))

dfs(a, b, c, 0)

if answer == sys.maxsize:
  answer = -1

print(answer)


import heapq

def dijkstra(start):
  global result
  h = []
  heapq.heappush(h, [0, 0, start])
  while h:
    max_cost, total_cost, now = heapq.heappop(h)
    if total_cost > c:
      continue
    for next_node, next_cost in graph[now]:
      cost = total_cost + next_cost
      if cost > c or visited[now][next_node]:
        continue
      if next_node == b:
        result = min(result, max(max_cost, next_cost))
      visited[now][next_node] = True
      heapq.heappush(h, [max(max_cost, next_cost), cost, next_node])

INF = int(1e9)
n, m, a, b, c = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  start, end, cost = map(int, input().split())
  graph[start].append((end, cost))
  graph[end].append((start, cost))

result = INF
visited = [[[False] for _ in range(n + 1)] for _ in range(n + 1)]

dijkstra(a)

if result != INF:
  print(result)
else:
  print(-1)

import sys

n, m, a, b, c = map(int, input().split())

INF = int(1e9)
board = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
answer = INF

def dfs(start, end, cost, maxShame):
  visited[start] = True
  global answer
  if start == end:
    answer = min(answer, maxShame)
    return
  for item in board[start]:
    next_node = item[0]
    next_cost = item[1]
    if visited[next_node] == True:
      continue
    if next_cost > c:
      continue
    visited[next_node] = True
    dfs(next_node, end, cost - next_cost, max(maxShame, next_cost))
    visited[next_node] = False

for _ in range(m):
  n1, n2, cost = map(int, input().split())
  board[n1].append((n2, cost))
  board[n2].append((n1, cost))

dfs(a, b, c, 0)

if answer == INF:
  answer = -1

print(answer)