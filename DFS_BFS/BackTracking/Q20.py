from itertools import combinations



n = int(input())

board = []
t_list = []
x_list = []
for row in range(n):
    temp = input().split()
    for col in range(n):
        if temp[col] == "X":
            x_list.append((row, col))
        elif temp[col] == "T":
            t_list.append((row, col))

    board.append(temp)


candidates = list(combinations(x_list, 3))

def check(t_list):
    global n
    for t_row, t_col in t_list:
        for idx in range(1, n):
            if t_col - idx > -1:
                if board[t_row][t_col - idx] == "O":
                    break
                if board[t_row][t_col - idx] == "S":
                    return False

        for idx in range(1, n):
            if t_col + idx < n:
                if board[t_row][t_col + idx] == "O":
                    break
                if board[t_row][t_col + idx] == "S":
                    return False

        for idx in range(1, n):
            if t_row - idx > -1:
                if board[t_row - idx][t_col] == "O":
                    break
                if board[t_row - idx][t_col] == "S":
                    return False

        for idx in range(1, n):
            if t_row + idx < n:
                if board[t_row - idx][t_col] == "O":
                    break
                if board[t_row - idx][t_col] == "S":
                    return False

    return True

def solution():
    for candidate in candidates:
        for row, col in candidate:
            board[row][col] = "O"
            
        # for _ in board:
        #     print(_)
        
        # print("")
        if check(t_list):
            return "YES"

        for row, col in candidate:
            board[row][col] = "X"

    return "NO"

print(solution())


import collections
import sys

input = sys.stdin.readline

n = int(input())
graph = [list(input().split()) for _ in range(n)]
dx = [-1, 1 ,0 , 0]
dy = [0, 0 , -1, 1]
queue = collections.deque()
check = False

def bfs():
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "T":
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            temp_x, temp_y = x, y
            while True:
                nx = temp_x + dx[i]
                ny = temp_y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == "X" and visited[nx][ny] == False:
                        visited[nx][ny] = True
                    elif graph[nx][ny] == "S":
                        return False
                    elif graph[nx][ny] == "O":
                        break
                    temp_x, temp_y = nx, ny
                else:
                    break

    return True

def recursive(index):
    global check
    if index == 3:
        if bfs():
            check = True
        return
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "X":
                graph[i][j] = "O"
                recursive(index + 1)
                graph[i][j] = "X"

recursive(0)
if check:
    print("YES")
else:
    print("NO")