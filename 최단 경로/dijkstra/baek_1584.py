# # 2022/08/24 Baek 1584

# from collections import deque
# import heapq

# INF = int(1e9)
# board = [[0 for _ in range(501)] for _ in range(501)]
# distance =[[INF for _ in range(501)] for _ in range(501)]

# n = int(input())
# for _ in range(n):
#   x1, y1, x2, y2 = map(int, input().split())
#   x1, x2 = min(x1, x2), max(x1, x2)
#   y1, y2 = min(y1, y2) , max(y1, y2)
#   for i in range(x1, x2 + 1):
#     for j in range(y1, y2 + 1):
#       if board[i][j] == 0:
#         board[i][j] = 1
        

# m = int(input())
# for _ in range(m):
#   x1, y1, x2, y2 = map(int, input().split())
#   x1, x2 = min(x1, x2), max(x1, x2)
#   y1, y2 = min(y1, y2) , max(y1, y2)
#   for i in range(x1, x2 + 1):
#     for j in range(y1, y2 + 1):
#       board[i][j] = 2

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def dijkstra(start_x, start_y):
#   q = []
#   heapq.heappush(q, (0, start_x, start_y))  # dist, x, y
#   distance[start_x][start_y] = 0
#   while q:
#     dist, now_x, now_y = heapq.heappop(q)
#     if distance[now_x][now_y] < dist:
#       continue
#     for idx in range(4):
#       nx = now_x + dx[idx]
#       ny = now_y + dy[idx]
#       if  0 <= nx <= 500 and 0 <= ny <= 500:
#         if board[nx][ny] == 2:
#           continue
#         elif board[nx][ny] == 1:
#           cost = dist + 1
#         else:
#           cost = dist
        
#         if cost < distance[nx][ny]:
#           distance[nx][ny] = cost
#           heapq.heappush(q, (cost, nx, ny))

# dijkstra(0, 0)
# result = distance[500][500]
# if result == INF:
#   print(-1)
# else:
#   print(result)









from collections import deque

INF = int(1e9)
board = [[0 for _ in range(501)] for _ in range(501)]
distance =[[-1 for _ in range(501)] for _ in range(501)]

n = int(input())
for _ in range(n):
  x1, y1, x2, y2 = map(int, input().split())
  x1, x2 = min(x1, x2), max(x1, x2)
  y1, y2 = min(y1, y2) , max(y1, y2)
  for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
      if board[i][j] == 0:
        board[i][j] = 1
        

m = int(input())
for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  x1, x2 = min(x1, x2), max(x1, x2)
  y1, y2 = min(y1, y2) , max(y1, y2)
  for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
      board[i][j] = 2

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]




# 다음에 갈곳이 안전지역이냐 위험지역이냐에 따라서 소모 생명력이 달라짐..
# 따라서 큐에 노드를 삽입할 때 위험지역(가중치 = 0)이면 큐의 왼쪽에 삽입되도록한다.
def bfs(start_x, start_y):
  queue = deque()
  queue.append((start_x, start_y))
  distance[start_x][start_y] = 0

  while queue:
    x, y = queue.popleft()
    for idx in range(4):
      nx = x + dx[idx]
      ny = y + dy[idx]
      if 0 <= nx <= 500 and 0 <= ny <= 500 and distance[nx][ny] == -1:
        if board[nx][ny] == 2:
          continue
        elif board[nx][ny] == 1:
          distance[nx][ny] = distance[x][y] + 1
          queue.append((nx, ny))
        else:
          distance[nx][ny] = distance[x][y]
          queue.appendleft((nx, ny))

        if nx == 500 and ny == 500:
          return

bfs(0,0)
print(distance[500][500])


