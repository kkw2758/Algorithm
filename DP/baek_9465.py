# 2021/06/28 Baek 9465

'''
import sys

read = sys.stdin.readline

t = int(read())

for i in range(t):
    n = int(read())
    board = []
    for _ in range(2):
        board.append(list(map(int, read().strip().split())))

    dp = [[0] * n for _ in range(2)]
    
    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    
    dp[0][1] = board[1][0] + board[0][1]
    dp[1][1] = board[0][0] + board[1][1]

    for j in range(2, n):
        dp[0][j] = board[0][j] + max(dp[1][j-1], dp[0][j-2], dp[1][j-2])
        dp[1][j] = board[1][j] + max(dp[0][j-1], dp[0][j-2], dp[1][j-2])

    print(max(dp[0][n-1], dp[1][n-1]))

'''

'''
import sys

read = sys.stdin.readline

t = int(read())

for i in range(t):
    n = int(read())
    board = []
    for _ in range(2):
        board.append(list(map(int, read().strip().split())))

    if n == 1:
        print(max(board[0][0], board[1][0]))
        continue
    
    board[0][1] = board[1][0] + board[0][1]
    board[1][1] = board[0][0] + board[1][1]

    
    for j in range(2, n):
        board[0][j] = board[0][j] + max(board[1][j-1], board[0][j-2], board[1][j-2])
        board[1][j] = board[1][j] + max(board[0][j-1], board[0][j-2], board[1][j-2])
        
    print(max(board[0][n-1], board[1][n-1]))
    '''