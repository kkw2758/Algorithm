m, n = map(int,input().split())
x, y, d = map(int,input().split())

move_types = [(-1,0), (0,1), (1,0), (0, -1)]

board = []
for i in range(m):
    board.append(list(map(int,input().split())))

board[x][y] = 2

count = 1
while True:
    move = False
    for i in range(4):
        nx = x + move_types[(d - 1 - i)%4][0]
        ny = y + move_types[(d - 1 - i)%4][1]

        if board[nx][ny] == 1:
            continue
        elif board[nx][ny] == 0:
            x = nx
            y = ny
            count += 1
            board[x][y] = 2
            move = True
            d = (d - 1 - x)%4
            break
   
    if not(move):
        nx = x - move_types[d][0]
        ny = y - move_types[d][1]
        if board[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny


print(count)
for x in board:
    print(x)