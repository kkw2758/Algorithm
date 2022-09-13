# from collections import deque
# import sys
# from this import d

# input = sys.stdin.readline

# n, k = map(int, input().split())
# board = []

# for _ in range(n):
#     temp = []
#     row = list(map(int, input().split()))
#     for r in row:
#         temp.append((r, 0))

#     board.append(temp)

# s, x, y = map(int, input().split())


# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     while q:
#         x, y = q.popleft()
#         for idx in range(4):
#             nx = x + dx[idx]
#             ny = y + dy[idx]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if board[nx][ny] == (0, 0) or board[x][y][1] < board[nx][ny][1] - 1:
#                     board[nx][ny] = (board[x][y][0], board[x][y][1] + 1)
#                     q.append((nx, ny))

# for i in range(1, k + 1):
#     for row in range(len(board)):
#         for col in range(len(board[0])):
#             if board[row][col] == (i, 0):
#                 bfs(row, col)


# if board[x - 1][y - 1] == 0 or board[x - 1][y - 1][1] > s:
#     print(0)
# else:
#     print(board[x -1][y - 1][0])



#solution
from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, s, x , y = q.popleft()

    if s == target_s:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])



from collections import deque

N, K = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

virus_list = []
for row in range(N):
    for col in range(N):
        if board[row][col] != 0:
            virus_list.append((board[row][col], row, col))

virus_list.sort()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(S):
    cnt = 0
    q = deque()
    for virus in virus_list:
        q.append((virus[1], virus[2]))
    while q:
        if cnt == S:
            return
        for i in range(len(q)):
            x, y = q.popleft()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] == 0:
                        board[nx][ny] = board[x][y]
                        q.append((nx, ny))

        cnt += 1

bfs(S)
print(board[X-1][Y-1])