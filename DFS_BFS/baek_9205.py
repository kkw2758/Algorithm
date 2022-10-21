# 2022/10/22 Baek 9205

#BFS
from collections import deque

def distance(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

def bfs(x, y):
  queue = deque()
  queue.append([x, y])
  visited = [False] * n

  while queue:
    x, y = queue.popleft()
    if distance(x, y, end_x, end_y) <= 1000:
      return True
    for i in range(n):
      if visited[i] == False:
        store_x, store_y = store[i]
        if distance(x, y, store_x, store_y) <= 1000:
          visited[i] = True
          queue.append((store_x, store_y))
  return False
for _ in range(int(input())):
  n = int(input())
  start_x, start_y = list(map(int, input().split()))
  store = [list(map(int, input().split())) for _ in range(n)]
  end_x, end_y = list(map(int, input().split()))
  visited = [False] * n
  check = bfs(start_x, start_y)
  print("happy" if check else "sad")


# DFS
def distance(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

def dfs(x, y, status):
  if distance(x, y, end_x, end_y) <= 1000:
    return True
  for i in range(n):
    store_x, store_y = store[i]
    if distance(x, y, store_x, store_y) <= 1000:
      if not visited[i]:
        visited[i] = True
        status = dfs(store_x, store_y, status)

  return status
for _ in range(int(input())):
  n = int(input())
  start_x, start_y = list(map(int, input().split()))
  store = [list(map(int, input().split())) for _ in range(n)]
  end_x, end_y = list(map(int, input().split()))
  visited = [False] * n
  check = dfs(start_x, start_y, False)
  print("happy" if check else "sad")