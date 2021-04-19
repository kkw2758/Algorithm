'''
def dfs_stack(x,y):
    stack = [(x,y)]
    area = 0

    while stack:
        x, y = stack.pop()
        if graph[x][y] == 1:
            continue
        
        graph[x][y] = 1
        area += 1

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1: 
                continue
            stack.append((nx, ny))


    return area


m, n, k = map(int,input().split())
graph = [[0] * m for _ in range(n)]


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 1


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result.append(dfs_stack(i,j))

result.sort()
print(len(result))
for member in result:
    print(member, end = " ")
'''

import sys
sys.setrecursionlimit(100000)

def dfs_recursive(x,y):
    area = 0
    
    if x < 0 or x > n - 1 or y < 0 or y > m - 1:
        return area

    if graph[x][y] == 1:
        return area
    
    graph[x][y] = 1
    area += 1

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        area += dfs_recursive(nx,ny)

    return area



m, n, k = map(int,input().split())
graph = [[0] * m for _ in range(n)]


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 1


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result.append(dfs_recursive(i,j))

result.sort()
print(len(result))
for member in result:
    print(member, end = " ")