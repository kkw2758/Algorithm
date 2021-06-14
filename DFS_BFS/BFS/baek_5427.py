'''
import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def fire_bfs(fire_list):
    queue = deque(fire_list)
    level = 1
    while queue:
        q_size = len(queue)
        for _ in range(q_size):
            x, y = queue.popleft()

            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if 0 <= nx < h and 0 <= ny < w:
                    if board[nx][ny] == ".":
                        board[nx][ny] = level
                        queue.append((nx, ny))
    


        level += 1

def start_bfs(start_x, start_y):
    if start_x == 0 or start_x == h - 1 or start_y == 0 or start_y == w -1:
        return 1
    queue = deque()
    queue.append((start_x, start_y))
    board[start_x][start_y] = 0

    while queue:
        x, y = queue.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            # nx와 ny의 범위가 맞고
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] == "#" or board[nx][ny] == "*":
                    continue

                if board[nx][ny] == "." or (board[x][y] + 1 < board[nx][ny]):
                    board[nx][ny] = board[x][y] + 1
                    if nx == 0 or nx == h - 1 or ny == 0 or ny == w - 1:
                        return board[nx][ny] + 1
                    queue.append((nx,ny))

    return "IMPOSSIBLE"


t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    
    fire_list = []
    board = []

    for row in range(h):
        tmp = list(input().strip())
        
        if "@" in tmp:
            start_x, start_y = row, tmp.index("@")

        fire_col = [ i for i, value in enumerate(tmp) if value == "*"]
        for col in fire_col:
            fire_list.append((row, col))

        board.append(tmp)
    
    fire_bfs(fire_list)

    print(start_bfs(start_x, start_y))
'''

from collections import deque
import sys

input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def escape(start_x, start_y, fire_list):
    if start_x == 0 or start_x == h - 1 or start_y == 0 or start_y == w -1:
        return 1
    queue = deque()
    queue.append((start_x, start_y))
    fire_queue = deque(fire_list)
    level = 1
    while queue:

        fire_queue_size = len(fire_queue)
        for _ in range(fire_queue_size):
            x, y = fire_queue.popleft()
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if 0 <= nx < h and 0 <= ny < w:
                    if board[nx][ny] == '.':
                        board[nx][ny] = '*'
                        fire_queue.append((nx, ny))       

        queue_size = len(queue)
        for _ in range(queue_size):
            x, y = queue.popleft()
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if 0 <= nx < h and 0 <= ny < w:
                    if board[nx][ny] == '.':
                        if nx == 0 or nx == h - 1 or ny == 0 or ny == w - 1:
                            return level + 1
                        board[nx][ny] = '@'
                        queue.append((nx, ny))

        level += 1

    return "IMPOSSIBLE"

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    
    fire_list = []
    board = []

    for row in range(h):
        tmp = list(input().strip())
        
        if "@" in tmp:
            start_x, start_y = row, tmp.index("@")

        fire_col = [ i for i, value in enumerate(tmp) if value == "*"]
        for col in fire_col:
            fire_list.append((row, col))

        board.append(tmp)

    print(escape(start_x, start_y, fire_list))