# from collections import deque

# n, m = map(int,input().split())
# graph = []

# for i in range(n):
#     graph.append(list(map(int,input().split())))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
    
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue

#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))

#     return graph[n - 1][m - 1]

# print(bfs(0, 0))
# for x in graph:
#     print(x)

# from collections import deque

# n, m = map(int, input().split())
# maze = [list(map(int, list(input()))) for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0 , -1 , 1]

# def bfs(x, y):

#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
#                 continue

#             if maze[nx][ny] == 1:
#                 maze[nx][ny] = maze[x][y] + 1
#                 queue.append((nx,ny))

#     return maze[n-1][m-1]

# print(bfs(0,0))
# for _ in maze:
#     print(_)





from collections import deque

def bfs(start_x, start_y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1 


n, m = map(int, input().split())
graph = [ list(map(int, list(input()))) for _ in range(n)]
bfs(0,0)
print(graph[n-1][m-1])