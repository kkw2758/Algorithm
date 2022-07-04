# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# for tc in range(int(input())):
#   n = int(input())
#   graph = []
#   for i in range(n):
#     graph.append(list(map(int, input().split())))

#   distance = [[INF] * n for _ in range(n)]

#   x, y = 0, 0
#   q = [(graph[x][y], x, y)]
#   distance[x][y] = graph[x][y]

#   while q:
#     dist, x, y  = heapq.heappop(q)
#     if distance[x][y] < dist:
#       continue
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
      
#       if nx < 0 or nx >= n or ny < 0 or ny >= n:
#         continue
      
#       cost = dist + graph[nx][ny]
#       if cost < distance[nx][ny]:
#         distance[nx][ny] = cost
#         heapq.heappush(q,(cost, nx, ny))
  
#   print(distance[n-1][n-1])



INF = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

distance = [[INF] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def get_smallest_node():
  min_value = INF
  index = 0,0
  for i in range(n):
    for j in range(n):
      if distance[i][j] < min_value and not visited[i][j]:
        index = i,j
        min_value = distance[i][j]

  return index

def dijkstra(start):
  start_x = start[0]
  start_y = start[1]
  distance[start_x][start_y] = graph[start_x][start_y]
  visited[start_x][start_y] = True
  for i in range(4):
    nx = start_x + dx[i]
    ny = start_y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
      continue
    distance[nx][ny] = distance[start_x][start_y] + graph[nx][ny]


  for i in range(n * n - 1):
    now_x, now_y = get_smallest_node()
    print(now_x, now_y)
    visited[now_x][now_y] = True
    for i in range(4):
      nx = now_x + dx[i]
      ny = now_y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      cost = distance[now_x][now_y] + graph[nx][ny]
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost

dijkstra((0,0))

# print(distance)
print(distance[n-1][n-1])
