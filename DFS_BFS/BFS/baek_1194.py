# 2023/03/16 Baek 1194

# 방문처리를 어떻게 할 것인가
# 열쇠가 있어야지 문을 열 수 있다.
# 0에서 부터 시작한다.
# 열쇠의 종류만큼 2차원 배열을 쌓는다

# import sys
# from collections import deque
# input = sys.stdin.readline

# N, M = map(int, input().split())
# board = []
# key_list = []
# for i in range(N):
#     board.append(list(input().strip()))
#     for j in range(M):
#         if 97 <= ord(board[i][j]) <= 122 and board[i][j] not in key_list:
#             key_list.append(board[i][j])
#         if board[i][j] == "0":
#             # 시작좌표 잡아주기
#             start_x, start_y = (i, j)

# visited = [[[-1] * M for _ in range(N)] for i in range(len(key_list) + 1)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(start_x, start_y):
#     # 시작좌표 방문처리 
#     visited[0][start_x][start_y] = 0
#     q = deque()
#     # x, y, keys
#     q.append((start_x, start_y, []))
#     # board를 순회하면서 찾은 키를 가지고 있어야함
#     keys = {}
#     while q:
#         x, y, keys = q.popleft()
#         if board[x][y] == "1":
#             return visited[len(keys)][x][y]
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 벽이 아니고 범위에 들어갈때
#             if (0 <= nx < N and 0 <= ny < M) and (board[nx][ny] != "#"):
#                 # 아직 방문 안했으면
#                 if visited[len(keys)][nx][ny] == -1:
#                     if 97 <= ord(board[nx][ny]) <= 122: # 만약 열쇠면
#                         if board[nx][ny] in keys: # 이미 가지고 있으면
#                           visited[len(keys)][nx][ny] = visited[len(keys)][x][y] + 1
#                           q.append((nx, ny, keys))
#                         else:
#                           visited[len(keys)][nx][ny] = visited[len(keys)][x][y] + 1
#                           visited[len(keys) + 1][nx][ny] = visited[len(keys)][x][y] + 1
#                           q.append((nx, ny, keys + [board[nx][ny]]))
                        
#                     elif 65 <= ord(board[nx][ny]) <= 90: # 문이면
#                         if board[nx][ny].lower() in keys: # 문에맞는 열쇠가 있다면
#                             visited[len(keys)][nx][ny] = visited[len(keys)][x][y] + 1
#                             q.append((nx, ny, keys))
#                     else:
#                         visited[len(keys)][nx][ny] = visited[len(keys)][x][y] + 1
#                         q.append((nx, ny, keys))
#     return -1

# print(bfs(start_x, start_y))
# for _ in board:
#     print(_)
# print()
# for visit in visited:
#     print(visit)



# from collections import deque
# import sys

# input = sys.stdin.readline

# def solve():
#     n, m = map(int, input().split())
#     board = [list(input().strip()) for _ in range(n)]
#     visit = [[-1] * m for _ in range(n)]
#     key = {"a":1, "b":2, "c":4, "d":8, "e":16, "f":32}
#     door = {"A":1, "B":2, "C":4, "D":8, "E":16, "F":32}
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     q = deque()
#     for i in range(n):
#         for j in range(m):
#             if board[i][j] == "0":
#                 q.append((i, j, 0, 0)) # x, y, cnt, bit masking
#                 visit[i][j] = 0
#                 board[i][j] = "."
#                 break
#         else:
#             continue
#         break

#     while q:
#         x, y, cnt, bit = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "#":
#                 if not visit[nx][ny] == -1 and visit[nx][ny] | bit == visit[nx][ny]:
#                     continue

#                 visit[nx][ny] = bit

#                 if board[nx][ny] == ".":
#                     q.append((nx, ny, cnt + 1, bit))

#                 if board[nx][ny] == "1":
#                     print(cnt + 1)
#                     sys.exit()

#                 k = key.get(board[nx][ny])
#                 if k != None:
#                     q.append((nx, ny, cnt + 1, bit|k))
#                     continue

#                 d = door.get(board[nx][ny])
#                 if d != None:
#                     if d | bit == bit:
#                         q.append((nx, ny, cnt + 1, bit))
#     print(-1)

# solve()

import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def haveKey(cur_key, door):
    value = cur_key & (1 << (ord(door) - ord('A')))
    return True if value else False

def bfs(x, y):
    q = deque([(x, y, 0, 0)])
    check = [[[False] * 64 for _ in range(50)] for _ in range(50)]
    check[x][y][0] = True

    while q:
        x, y, cnt, key = q.popleft()
        if board[x][y] == '1':
            return cnt
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if not check[nx][ny][key]:
                    if board[nx][ny] == '1' or board[nx][ny] == '.':
                        check[nx][ny][key] = True
                        q.append((nx, ny, cnt + 1, key))
                    elif 'a' <= board[nx][ny] <= 'f':
                        tmp_key = key | (1 << (ord(board[nx][ny]) - ord('a')))
                        check[nx][ny][tmp_key] = True
                        q.append((nx, ny, cnt + 1, tmp_key))
                    elif 'A' <= board[nx][ny] <= 'Z':
                        if haveKey(key, board[nx][ny]):
                            check[nx][ny][key] = True
                            q.append((nx, ny, cnt + 1, key))
    return -1

N, M = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            sx, sy = i, j
            board[i][j] = '.'
print(bfs(sx, sy))