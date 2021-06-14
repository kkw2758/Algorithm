from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    water_queue = deque(water_list)

    level = 1

    while queue:
        water_queue_size = len(water_queue)
        for _ in range(water_queue_size):
            x, y = water_queue.popleft()
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if 0 <= nx < R and 0 <= ny < C:
                    if board[nx][ny] == '.':
                        board[nx][ny] = '*'
                        water_queue.append((nx, ny))

        queue_size = len(queue)
        for _ in range(queue_size):
            x, y = queue.popleft()
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if 0 <= nx < R and 0 <= ny < C:            
                    if board[nx][ny] == '.':
                        board[nx][ny] = 'S'
                        queue.append((nx, ny))
                    elif board[nx][ny] == 'D':
                        return level

        level += 1

    return "KAKTUS"

R, C = map(int, input().split())
board = []
water_list = []
for row in range(R):
    tmp = list(input().strip())
    if "S" in tmp:
        start_x = row
        start_y = tmp.index("S")
    for col in range(len(tmp)):
        if tmp[col] == "*":
            water_list.append((row,col))


    board.append(tmp)

print(bfs(start_x, start_y))