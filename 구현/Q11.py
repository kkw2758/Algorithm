n = int(input())
board = []

for _ in range(n + 2):
    board.append([0] * (n + 2))

for i in range(len(board)):
    for j in range(len(board[0])):
        if (i == 0 or i == n + 1) or (j == 0 or j == n + 1):
            board[i][j] = -1



k = int(input())
for i in range(k):
    row, col = map(int, input().split())
    board[row][col] = 1

l = int(input())
direction_list = []
for i in range(l):
    second, direction = input().split()
    second = int(second)
    direction_list.append((second, direction))


# R D L U
dx = [0, 1, 0 , -1]
dy = [1, 0, -1, 0]

def solution():
    cnt = 0
    x, y = 1, 1
    board[x][y] = 2
    direction = 0
    body_list = [(1,1)]
    while True:
        if direction_list:
            temp = direction_list[0]
            if cnt == temp[0]:
                if temp[1] == "L":
                    direction = (direction - 1) % 4
                elif temp[1] == "D":
                    direction = (direction + 1) % 4
                direction_list.pop(0)
        #앞으로 가자
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if board[nx][ny] == -1 or board[nx][ny] == 2:
            return cnt + 1
        elif board[nx][ny] == 1: #사과 있으면!
            body_list.append((nx, ny))
            board[nx][ny] = 2
        else:
            body_list.append((nx, ny))
            board[nx][ny] = 2
            if body_list:
                tx, ty = body_list.pop(0)
                board[tx][ty] = 0

        cnt += 1
        x, y = nx, ny

print(solution())

'''
ex1)
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

ex2)
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

ex3)
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
'''