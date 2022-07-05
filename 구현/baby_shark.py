# from collections import deque
# from copy import deepcopy

# n = int(input())

# graph = []

# for i in range(n):
#     graph.append(list(map(int, input().split())))

# def find_start_point(graph):
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == 9:
#                 return i,j

# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]

# def bfs(start_x, start_y, shark_size, count):
#     q = deque()
#     q.append((start_x, start_y))
#     temp_graph = deepcopy(graph)
    
#     while q:
#         x, y = q.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if 0 < temp_graph[nx][ny] < shark_size:
#                     graph[nx][ny] = 9
#                     graph[start_x][start_y] = 0
#                     time = temp_graph[x][y] - 8 
#                     count += 1
#                     if count == shark_size:
#                         shark_size += 1
#                         count = 0

#                     return time, shark_size, count

#                 if temp_graph[nx][ny] == shark_size or temp_graph[nx][ny] == 0:
#                     temp_graph[nx][ny] = temp_graph[x][y] + 1
#                     q.append((nx, ny))

#     return 0, shark_size, count

# total_time = 0
# shark_size = 2
# count = 0
# while True:
#     start_x, start_y = find_start_point(graph)
#     time, shark_size, count = bfs(start_x, start_y, shark_size, count)
#     if time == 0:
#         break
#     total_time += time
    

# print(total_time)

from collections import deque
INF = 1e9

n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

now_size = 2
now_x, now_y = 0, 0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0
            break
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((now_x, now_y))
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] < now_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]

    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        array[now_x][now_y] = 0
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0
