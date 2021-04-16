import sys
sys.setrecursionlimit(10000000)
'''
def dfs(x, y):
    if board[x][y] == 0:
        return False

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    board[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        else:
            dfs(nx, ny)

    return True

T = int(input())
result = []
for t in range(T):
    cnt = 0
    N, M, K = map(int,input().split())
    board = [[0 for i in range(N)] for j in range(M)]
    
    

    for _ in range(K):
        x, y = map(int,input().split())
        board[y][x] = 1


    for y in range(N):
        for x in range(M):
            if dfs(x,y):
                cnt += 1


    result.append(cnt)

for x in result:
    print(x)
'''



def dfs(x, y):
    if x < 0 or x > M - 1 or y < 0 or y > N - 1:
        return False
    
    if board[x][y] == 1:
        board[x][y] = 0

        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        
        return True

    return False



T = int(input())
result = []
for t in range(T):
    cnt = 0
    N, M, K = map(int,input().split())
    board = [[0 for i in range(N)] for j in range(M)]
    
    

    for _ in range(K):
        x, y = map(int,input().split())
        board[y][x] = 1


    for y in range(N):
        for x in range(M):
            if dfs(x,y):
                cnt += 1


    result.append(cnt)

for x in result:
    print(x)