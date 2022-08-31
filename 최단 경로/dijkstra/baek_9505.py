# 2022/08/31 Baek 9505

import sys, heapq

INF = int(1e9)
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dijkstra(start_x, start_y):
  distance = [[INF] * W for _ in range(H)]
  q = []
  heapq.heappush(q, (0, start_x, start_y))
  distance[start_x][start_y] = 0

  while q:
    cost, now_x, now_y = heapq.heappop(q)
    if distance[now_x][now_y] < cost:
      continue
    if now_x == 0 or now_x == H - 1 or now_y == 0 or now_y == W - 1:
      return distance[now_x][now_y]
    for idx in range(4):
      nx = now_x + dx[idx]
      ny = now_y + dy[idx]
      if 0 <= nx < H and 0 <= ny < W:
        if graph[nx][ny] != "E":
          next_cost = cost + classes[graph[nx][ny]]
          if next_cost < distance[nx][ny]:
            distance[nx][ny] = next_cost
            heapq.heappush(q, (next_cost, nx, ny))

T = int(input())
for i in range(T):
  K, W, H = map(int, input().split())
  classes = {}

  for _ in range(K):
    name, time = input().split()
    classes[name] = int(time)

  graph = []
  E_position = 0
  for row in range(H):
    temp = list(input().rstrip())
    graph.append(temp)
    if "E" in temp:
      for col in range(len(temp)):
        if temp[col] == "E":
          E_position = (row, col)

  print(dijkstra(E_position[0], E_position[1]))