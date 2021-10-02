# import sys
# from collections import deque

# input = sys.stdin.readline
# n, m = map(int, input().split())
# graph = [[0 for _ in range(m + 1)]]

# for _ in range(n):
#     graph.append([0] + list(map(int,list(input().strip()))))


# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]

# def bfs():
#     queue = deque()
#     queue.append((1,1))
#     while queue:
#         x,y = queue.popleft()
#         for idx in range(4):
#             nx = x + dx[idx]
#             ny = y + dy[idx]
#             #범위 밖인덱스
#             if nx < 1 or nx > n or ny < 1 or ny > m:
#                 continue
#             if graph[nx][ny] == 1:
#                 queue.append((nx, ny))
#                 graph[nx][ny] = graph[x][y] + 1


# bfs()
# print(graph[n][m])


#복습
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
table = []
for _ in range(n):
    row = map(int, list(input().strip()))
    table.append(list(row))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
            
            if table[nx][ny] == 1:
                table[nx][ny] = table[x][y] + 1
                queue.append((nx,ny))

    return table[n-1][m-1]
    

print(bfs(0,0))