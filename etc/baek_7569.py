# 2022/09/02 Baek 7569

import sys, heapq

input = sys.stdin.readline
INF = int(1e9)
M, N, H = map(int, input().split())
graph = [[[0] * M for _ in range(N)] for _ in range(H)]
distance = [[[INF] * M for _ in range(N)] for _ in range(H)]

tomatoes = []
for z in range(H):
  for y in range(N):
    temp = list(map(int, input().rstrip().split()))
    for x in range(M):
      if temp[x] == 1:
        tomatoes.append((z, y, x))
      graph[z][y][x] = temp[x]

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def dijkstra(start_index_list):
  q = []
  for z, y, x in start_index_list:
    heapq.heappush(q, (0, z, y, x))
    distance[z][y][x] = 0
  
  while q:
    dist, z, y, x = heapq.heappop(q)
    if distance[z][y][x] < dist:
      continue
    for idx in range(6):
      nx = x + dx[idx]
      ny = y + dy[idx]
      nz = z + dz[idx]
      if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
        if graph[nz][ny][nx] == 0:
          graph[nz][ny][nx] = 1
        elif graph[nz][ny][nx] == -1:
          continue
        cost = dist + 1
        if cost < distance[nz][ny][nx]:
          distance[nz][ny][nx] = cost
          heapq.heappush(q, (cost, nz, ny, nx))

dijkstra(tomatoes)

def check_result():
  max_value = 0
  for z in range(H):
    for y in range(N):
      for x in range(M):
        if graph[z][y][x] == 0:
          return -1
        if graph[z][y][x] == 1:
          max_value = max(max_value, distance[z][y][x])
  return max_value

print(check_result())