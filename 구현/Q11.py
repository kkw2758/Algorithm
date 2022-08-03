# n = int(input())
# board = []

# for _ in range(n + 2):
#     board.append([0] * (n + 2))

# for i in range(len(board)):
#     for j in range(len(board[0])):
#         if (i == 0 or i == n + 1) or (j == 0 or j == n + 1):
#             board[i][j] = -1



# k = int(input())
# for i in range(k):
#     row, col = map(int, input().split())
#     board[row][col] = 1

# l = int(input())
# direction_list = []
# for i in range(l):
#     second, direction = input().split()
#     second = int(second)
#     direction_list.append((second, direction))


# # R D L U
# dx = [0, 1, 0 , -1]
# dy = [1, 0, -1, 0]

# def solution():
#     cnt = 0
#     x, y = 1, 1
#     board[x][y] = 2
#     direction = 0
#     body_list = [(1,1)]
#     while True:
#         if direction_list:
#             temp = direction_list[0]
#             if cnt == temp[0]:
#                 if temp[1] == "L":
#                     direction = (direction - 1) % 4
#                 elif temp[1] == "D":
#                     direction = (direction + 1) % 4
#                 direction_list.pop(0)
#         #앞으로 가자
#         nx = x + dx[direction]
#         ny = y + dy[direction]
        
#         if board[nx][ny] == -1 or board[nx][ny] == 2:
#             return cnt + 1
#         elif board[nx][ny] == 1: #사과 있으면!
#             body_list.append((nx, ny))
#             board[nx][ny] = 2
#         else:
#             body_list.append((nx, ny))
#             board[nx][ny] = 2
#             if body_list:
#                 tx, ty = body_list.pop(0)
#                 board[tx][ty] = 0

#         cnt += 1
#         x, y = nx, ny

# print(solution())

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

n = int(input())
arr = [[0] * n for _ in range(n)]

k = int(input())

for _ in range(k):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 2

l = int(input())
direction_information = []
for _ in range(l):
    x, d = input().split()
    direction_information.append((int(x), d))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


snake_list = [(0, 0)]
arr[0][0] = 1
direction_idx = 1
cnt = 0

while True:
    x, y = snake_list[-1]
    # if direction_information:
    #     if cnt == direction_information[0][0]:
    #         direction = direction_information.pop(0)[1]
    #         if direction == "D":
    #             direction_idx = (direction_idx + 1) % 4
    #         else:
    #             direction_idx = (direction_idx - 1) % 4

    # print("now_direction = {}".format(direction_idx))
    nx, ny = x + dx[direction_idx], y + dy[direction_idx]
    cnt += 1
    if not(0 <= nx < n and 0 <= ny < n):    # 범위안에 안들어오면
        break
    else:
        if arr[nx][ny] == 2:    # 사과면
            snake_list.append((nx, ny))
            arr[nx][ny] = 1
        elif arr[nx][ny] == 1:   # 뱀 몸뚱아리면
            break
        else:   # 사과도 아니고 몸뚱아리도 아니면
            snake_list.append((nx, ny))
            arr[nx][ny] = 1
            pop_x, pop_y = snake_list.pop(0)
            arr[pop_x][pop_y] = 0
    
    if direction_information:
        if cnt == direction_information[0][0]:
            direction = direction_information.pop(0)[1]
            if direction == "D":
                direction_idx = (direction_idx + 1) % 4
            else:
                direction_idx = (direction_idx - 1) % 4

    print("now_direction = {}".format(direction_idx))

    print(cnt)
    for _ in arr:
        print(_)
    print("=" * 50)

print("result = {}".format(cnt))