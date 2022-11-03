# 2022/11/03 baek 14923

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

distance = [[[-1] * M for _ in range(N)] for _ in range(2)]
def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    distance[0][x][y] = 0
    while q:
        x, y, flag = q.popleft()
        if [x, y] == [Ex - 1, Ey - 1]:
            return distance[flag][x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if flag == 0:
                    if graph[nx][ny] == 0 and distance[0][nx][ny] == -1:
                        q.append((nx, ny, 0))
                        distance[0][nx][ny] = distance[0][x][y] + 1
                        
                    elif graph[nx][ny] == 1 and distance[1][nx][ny] == -1:
                        q.append((nx, ny, 1))
                        distance[1][nx][ny] = distance[0][x][y] + 1
                else:
                    if graph[nx][ny] == 0 and distance[1][nx][ny] == -1:
                        q.append((nx, ny, 1))
                        distance[1][nx][ny] = distance[1][x][y] + 1
    return - 1

result = bfs(Hx - 1, Hy - 1)
print(result)