# import heapq

# def dijkstra(start_x, start_y):
#   start = start_x * n + start_y + 1
#   dist = graph[start_x][start_y]

#   q = []
#   heapq.heappush(q, (dist, start)) #거리 시작 노드
#   distance[start] = dist
  
#   while q:
#     dist, now = heapq.heappop(q)
#     if dist > distance[now]:
#       continue
#     for next_node in distance_information[now]:
#       cost = dist + next_node[1]
#       if cost < distance[next_node[0]]:
#         distance[next_node[0]] = cost
#         heapq.heappush(q, (cost, next_node[0]))

# t = int(input())        

# for i in range(t):
#   n = int(input())
#   INF = int(1e9)
#   graph = []

#   for i in range(n):
#     graph.append(list(map(int, input().split())))

#   distance_information = [[] for _ in range(n * n  + 1)]
#   distance = [INF] * (n * n + 1)

#   dx = [-1, 0, 1, 0]
#   dy = [0, 1, 0, -1]
#   dnode = [-n, 1, n, - 1]
#   node = 1
#   for i in range(n):
#     for j in range(n):
      
#       for idx in range(4):
#         nx, ny = i + dx[idx], j + dy[idx]
#         if 0 <= nx < n and 0 <= ny < n:
#           distance_information[node].append((node + dnode[idx], graph[nx][ny]))  #노드번호, 거리

#       node += 1

#   # for _ in distance_information:
#   #   print(_)

#   dijkstra(0,0)
#   print(distance[n * n])


import heapq

INF = int(1e9)
n = int(input())
graph = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

distance = [[INF] * n for _ in range(n)]

q = []
heapq.heappush(q, ((graph[0][0]), 0, 0))
distance[0][0] = graph[0][0]

while q:
  dist, x, y = heapq.heappop(q)
  if dist > distance[x][y]:
    continue
  
  for idx in range(4):
    nx = x + dx[idx]
    ny = y + dy[idx]
    if 0 <= nx < n and 0 <= ny < n:
      cost = dist + graph[nx][ny]
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost
        heapq.heappush(q, (cost, nx, ny))

print(distance[n - 1][n - 1])