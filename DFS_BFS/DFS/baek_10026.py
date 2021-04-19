'''
def dfs(x, y, color, board):
    if board[x][y] == 0:
        return
    if board[x][y] != color:
        return
    
    #방문 체크
    board[x][y] = 0
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
            continue
        dfs(nx, ny, color, board)


def RG_dfs(x, y, color, board):
    if board[x][y] == 0:
        return

    if color == "R" or color == "G":
        if board[x][y] == "B":
            return
        board[x][y] = 0
    else:#color = B
        if board[x][y] == "B":
            board[x][y] = 0
        else:
            return

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
            continue
        RG_dfs(nx, ny, color, board)

import sys
import copy

sys.setrecursionlimit(100000)

n = int(input())
board1 = []

for _ in range(n):
    board1.append(list(input()))

board2 = copy.deepcopy(board1)
dx = [0 ,0, -1, 1]
dy = [1, -1, 0, 0]

result = 0

for i in range(n):
    for j in range(n):
        if board1[i][j] != 0:
            result += 1
            dfs(i, j, "R", board1)
            dfs(i, j, "G", board1)
            dfs(i, j, "B", board1)

print(result)

result = 0

for i in range(n):
    for j in range(n):
        if board2[i][j] != 0:
            result += 1
            RG_dfs(i, j, "R", board2)
            RG_dfs(i, j, "G", board2)
            RG_dfs(i, j, "B", board2)

print(result)
'''

'''
#!/usr/bin/python3

import copy

d0 = [0,-1,0,1]
d1 = [1,0,-1,0]

n = int(input())
temp = [list(input().strip()) for _ in range(n)]

def bfs(v, C):
	q = [v]
	while q:
		cur = q[0]
		q.remove(q[0])
		for k in range(4):
			new = cur[0] + d0[k], cur[1] + d1[k]
			if 0 <= new[0] < n and 0 <= new[1] < n and paint[new[0]][new[1]] in C:
				paint[new[0]][new[1]] = 'X'
				q.append([new[0],new[1]])

paint = copy.deepcopy(temp)
cnt1 = 0
for i in range(n):
	for j in range(n):
		if paint[i][j] != 'X':
			cnt1 += 1
			bfs([i,j],[paint[i][j]])

paint = copy.deepcopy(temp)
cnt2 = 0
for i in range(n):
	for j in range(n):
		if paint[i][j] in ['R','G']:
			cnt2 += 1
			bfs([i,j],['R','G'])
		if paint[i][j] == 'B':
			cnt2 += 1
			bfs([i,j],['B'])
print(cnt1,cnt2)
'''

import copy

n = int(input())
board = [list(input()) for _ in range(n)]
temp = copy.deepcopy(board)


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0] 


def dfs_stack(x, y, colors):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if board[x][y] == "0":
            continue
        
        if board[x][y] not in colors:
            continue

        board[x][y] = "0"


        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            
            if 0 <= nx <= n - 1 and 0 <= ny <= n - 1:
                stack.append((nx,ny))

result = 0

for i in range(n):
    for j in range(n):
        if board[i][j] != "0":
            dfs_stack(i,j,board[i][j])
            result += 1


print(result)

board = temp

result = 0

for i in range(n):
    for j in range(n):
        if board[i][j] != "0":
            dfs_stack(i,j,["B"])
            dfs_stack(i,j,["R","G"])
            result += 1

print(result)