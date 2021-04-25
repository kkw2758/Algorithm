'''
import sys
from collections import deque

input = sys.stdin.readline

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    dx = [-1, 1, -2, 2, -2, 2, -1, 1]
    dy = [2, 2, 1, 1, -1, -1, -2, -2]
    
    while queue:
        x,y = queue.popleft()

        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if nx < 0 or nx > l - 1 or ny < 0 or ny > l - 1:
                continue
            if not graph[nx][ny]: 
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

t = int(input())
for _ in range(t):
    l = int(input())
    graph = [[0]*(l) for _ in range(l)]
    start_x, start_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())

    if start_x == dest_x and start_y == dest_y:
        print(0)
    else:
        bfs(start_x, start_y)
        print(graph[dest_x][dest_y])
        '''

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    dx = [-1, 1, -2, 2, -2, 2, -1, 1]
    dy = [2, 2, 1, 1, -1, -1, -2, -2]
    
    while queue:
        x,y = queue.popleft()
        if x == dest_x and y == dest_y:
            return graph[x][y]
        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if nx < 0 or nx > l - 1 or ny < 0 or ny > l - 1:
                continue
            if not graph[nx][ny]: 
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

t = int(input())
for _ in range(t):
    l = int(input())
    graph = [[0]*(l) for _ in range(l)]
    start_x, start_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())

    print(bfs(start_x,start_y))