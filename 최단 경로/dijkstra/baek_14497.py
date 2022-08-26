# 2022/08/26 Baek 14497

# import heapq
# import sys

# INF = int(1e9)
# input = sys.stdin.readline
# n, m = map(int, input().split())
# graph = [[]]
# x1, y1, x2, y2 = map(int, input().split())

# for _ in range(n):
#   graph.append([0] +list(input().rstrip()))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dijkstra(start_x, start_y):
#   distance = [[INF] * (m + 1) for _ in range(n + 1)]
#   q = []
#   heapq.heappush(q, (0, start_x, start_y))
#   distance[start_x][start_y] = 0
#   friends = set()
#   while q:
#     dist, x, y = heapq.heappop(q)
#     if distance[x][y] < dist:
#       continue
#     for idx in range(4):
#       nx = x + dx[idx]
#       ny = y + dy[idx]
#       if 1 <= nx <= n and 1 <= ny <= m:
#         if graph[nx][ny] == "#":
#           return True
#         if graph[nx][ny] == "0":
#           cost = dist + 1
#           if cost < distance[nx][ny]:
#             distance[nx][ny] = cost
#             heapq.heappush(q, (cost, nx, ny))
#         else:
#           friends.add((nx, ny))
  
#   # friends = list(friends)
#   for x, y in friends:
#     graph[x][y] = "0"

#   return False

# cnt = 1
# while not(dijkstra(x1, y1)):
#   cnt += 1

# print(cnt)


import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[]]
x1, y1, x2, y2 = map(int, input().split())

for _ in range(n):
  graph.append([0] +list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(start_x, start_y):
  distance = [[INF] * (m + 1) for _ in range(n + 1)]
  q = []
  heapq.heappush(q, (1, start_x, start_y))
  distance[start_x][start_y] = 1
  while q:
    dist, x, y = heapq.heappop(q)
    if distance[x][y] < dist:
      continue
    for idx in range(4):
      nx = x + dx[idx]
      ny = y + dy[idx]
      if 1 <= nx <= n and 1 <= ny <= m:
        if graph[nx][ny] == "#":
          return dist
        if graph[nx][ny] == "0":
          cost = dist
          if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))
        else:
          cost = dist + 1
          if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))

print(dijkstra(x1, y1))