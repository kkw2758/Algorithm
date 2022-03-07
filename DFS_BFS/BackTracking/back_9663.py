# import copy
# n = int(input())

# board = [[False] * n for _ in range(n)]
# result = 0

# def visit(x, y):
#     dx = [-1, -1, 1, 1]
#     dy = [-1, 1, 1, -1]
#     for i in range(n):
#         board[x][i] = True
#         board[i][y] = True
#     for i in range(4):
#         for j in range(1,n):
#             nx = x + dx[i] * j
#             ny = y + dy[i] * j
#             if (0 <= nx <= n - 1) and (0 <= ny <= n - 1):
#                 board[nx][ny] = True

# def dfs(cnt):
#     global result, board
#     if cnt == n:
#         result += 1
#         return

#     for i in range(n):
#         if board[cnt][i] == False:
#             temp_board = copy.deepcopy(board)
#             visit(cnt, i)       
#             # print("방문",cnt, i)
#             # for _ in board:
#             #     print(_)
#             dfs(cnt + 1)
#             board = temp_board
#             # print("방문 캔슬", cnt, i)
#             # for _ in board:
#             #     print(_)

# dfs(0)
# print(result)


n = int(input())

answer = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True

def n_queens(x):
    global answer
    if x == n:
        answer += 1

    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)

n_queens(0)
print(answer)