import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    board[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            # nx와 ny의 범위가 맞고
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] == ".":
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx,ny))
                
                '''
                아래주석 부분 수정필요
                '''
                #elif str(type(board[nx][ny])) == "<class 'int'>":
                    # print("핳")
                    # board[nx][ny] = min(board[nx][ny], board[x][y] + 1)
                    # queue.append((nx,ny))


t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    
    fire_list = []
    board = []

    for row in range(h):
        tmp = list(input().strip())
        board.append(tmp)
        fire_col = [ i for i, value in enumerate(tmp) if value == "*"]
        for col in fire_col:
            fire_list.append((row, col)) 

    print(fire_list)
    print(board)
    for fire in fire_list:
        print(fire)
        bfs(fire[0], fire[1])
        print(board)