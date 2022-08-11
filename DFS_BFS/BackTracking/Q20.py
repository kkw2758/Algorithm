# from itertools import combinations
# n = int(input())

# board = []
# t_list = []
# x_list = []
# for row in range(n):
#     temp = input().split()
#     for col in range(n):
#         if temp[col] == "X":
#             x_list.append((row, col))
#         elif temp[col] == "T":
#             t_list.append((row, col))

#     board.append(temp)


# candidates = list(combinations(x_list, 3))

# def check(t_list):
#     global n
#     for x, y in t_list:
#         for idx in range(1, n):
#             if y - idx > -1:
#                 if board[x][y - idx] == "O":
#                     break
#                 if board[x][y - idx] == "S":
#                     return False

#         for idx in range(1, n):
#             if y + idx < n:
#                 if board[x][y + idx] == "O":
#                     break
#                 if board[x][y + idx] == "S":
#                     return False

#         for idx in range(1, n):
#             if x - idx > -1:
#                 if board[x - idx][y] == "O":
#                     break
#                 if board[x - idx][y] == "S":
#                     return False

#         for idx in range(1, n):
#             if x + idx < n:
#                 if board[x - idx][y] == "O":
#                     break
#                 if board[x - idx][y] == "S":
#                     return False

#     return True

# def solution():
#     for candidate in candidates:
#         for row, col in candidate:
#             board[row][col] = "O"
            
#         # for _ in board:
#         #     print(_)
        
#         # print("")
#         if check(t_list):
#             return "YES"

#         for row, col in candidate:
#             board[row][col] = "X"

#     return "NO"

# print(solution())


# import collections
# import sys

# input = sys.stdin.readline

# n = int(input())
# graph = [list(input().split()) for _ in range(n)]
# dx = [-1, 1 ,0 , 0]
# dy = [0, 0 , -1, 1]
# queue = collections.deque()
# check = False

# def bfs():
#     visited = [[False] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == "T":
#                 queue.append((i,j))

#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             temp_x, temp_y = x, y
#             while True:
#                 nx = temp_x + dx[i]
#                 ny = temp_y + dy[i]
#                 if 0 <= nx < n and 0 <= ny < n:
#                     if graph[nx][ny] == "X" and visited[nx][ny] == False:
#                         visited[nx][ny] = True
#                     elif graph[nx][ny] == "S":
#                         return False
#                     elif graph[nx][ny] == "O":
#                         break
#                     temp_x, temp_y = nx, ny
#                 else:
#                     break

#     return True

# def recursive(index):
#     global check
#     if index == 3:
#         if bfs():
#             check = True
#         return
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == "X":
#                 graph[i][j] = "O"
#                 recursive(index + 1)
#                 graph[i][j] = "X"

# recursive(0)
# if check:
#     print("YES")
# else:
#     print("NO")


# from itertools import combinations
# from copy import deepcopy

#학생 찾기가 불가능하면 True    
# def check(board, x, y):
#     n = len(board)
#     #위
#     for i in range(x - 1, -1, -1):
#         if board[i][y] == "S":
#             return False
#         elif board[i][y] == "O":
#             break
#     #아래
#     for i in range(x + 1, n):
#         if board[i][y] == "S":
#             return False
#         elif board[i][y] == "O":
#             break
#     #왼쪽
#     for i in range(y - 1, -1, -1):
#         if board[x][i] == "S":
#             return False
#         elif board[x][i] == "O":
#             break
#     #오른쪽
#     for i in range(y + 1, n):
#         if board[x][i] == "S":
#             return False
#         elif board[x][i] == "O":
#             break

#     return True

# def solution():
#     N = int(input())
#     board = []

#     for _ in range(N):
#         board.append(list(input().split()))
#     teachers = []
#     empty_areas = []
#     for row in range(N):
#         for col in range(N):
#             if board[row][col] == "X":
#                 empty_areas.append((row, col))
#             elif board[row][col] == "T":
#                 teachers.append((row, col))

#     candidates = combinations(empty_areas, 3)
#     for candidate in candidates:
#         flag = True

#         for row, col in candidate:
#             board[row][col] = "O"
        
#         for teacher in teachers:
#             if not(check(board, teacher[0], teacher[1])):
#                 flag = False

#         for row, col in candidate:
#             board[row][col] = "X"
            
#         if flag == True:
#             return "YES"

#     return "NO"

# print(solution())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < N and 0 <= ny < N and board[nx][ny] != "O":
            if board[nx][ny] == "S":
                return False
            else:
                nx += dx[i]
                ny += dy[i]

    return True

N = int(input())
board = []
answer = False

for _ in range(N):
    board.append(list(input().split()))
teachers = []
empty_areas = []
for row in range(N):
    for col in range(N):
        if board[row][col] == "X":
            empty_areas.append((row, col))
        elif board[row][col] == "T":
            teachers.append((row, col))

def dfs(count, board):
    global answer
    if count == 3:
        flag = True
        for teacher in teachers:
            if not(check(teacher[0], teacher[1])):
                flag = False

        if flag == True:
            answer = True

        return
    else:
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == "X":
                    board[row][col] = "O"
                    count += 1
                    dfs(count, board)
                    board[row][col] = "X"
                    count -= 1

dfs(0, board)
if answer:
    print("YES")
else:
    print("NO")