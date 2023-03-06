# 2023/03/06 Baek 16507
import sys
input = sys.stdin.readline

R, C, Q = map(int, input().split())
board = [[0] * (C + 1)]
for _ in range(R):
    board.append([0] + list(map(int, input().split())))

targets = []
for _ in range(Q):
    targets.append(list(map(int, input().split())))

for i in range(1, R + 1):
    for j in range(1, C + 1):
        board[i][j] += board[i - 1][j] + board[i][j - 1] - board[i - 1][j - 1]
        
for target in targets:
    total = board[target[2]][target[3]] - board[target[2]][target[1] - 1] - board[target[0] - 1][target[3]] + board[target[0]-1][target[1]-1]
    result = int(total / ((target[2] - target[0] + 1) * (target[3] - target[1] + 1)))
    print(result)
