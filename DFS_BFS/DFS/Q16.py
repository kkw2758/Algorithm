# from itertools import combinations
# import copy
# import sys

# input = sys.stdin.readline

# empty_location_list = []

# n, m = map(int, input().split())

# board = [[-1] * (m + 1) for _ in range(n + 1)]

# for row in range(1, n + 1):
#     temp = list(map(int, input().split()))
#     for col in range(len(temp)):
#         board[row][col + 1] = temp[col]
#         if temp[col] == 0:
#             empty_location_list.append((row, col + 1))

# candidates = list(combinations(empty_location_list, 3))


# def dfs(x, y):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     stack = [(x,y)]
#     while stack:
#         x, y = stack.pop()
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if (1 <= nx <= n) and (1 <= ny <= m):
#                 if temp_board[nx][ny] == 0:
#                     stack.append((nx, ny))
#                     temp_board[nx][ny] = 2



# result = 0

# for candidate in candidates:
#     temp_board = copy.deepcopy(board)
#     for x, y in candidate:
#         temp_board[x][y] = 1


#     for x in range(1, n + 1):
#         for y in range(1, m + 1):
#             if temp_board[x][y] == 2:
#                 dfs(x,y)

#     cnt = 0
#     for x in range(1, n + 1):
#         for y in range(1, m + 1):
#             if temp_board[x][y] == 0:
#                 cnt += 1

#     result = max(result, cnt)

# print(result)




n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score
    
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)

        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)