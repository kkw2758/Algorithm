n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, list(input()))))

def dfs(x,y):
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y- 1 )
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result += 1

print(result)



# 복습
n, m = map(int, input().split())
table = [list(map(int, list(input()))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]

def dfs(x,y):
    table[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
            continue
        if table[nx][ny] == 0:
            dfs(nx,ny)
                
result = 0

for row in range(n):
    for col in range(m):
        if table[row][col] == 0: # 구멍뚫려있으면
            result += 1
            dfs(row, col)

print(result)

'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
    
def ice_juice(graph):
    cnt = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 0:
                cnt += 1
                stack = []
                stack.append((y,x))
                graph[y][x] = 1
            
                while stack:
                    ay,ax = stack.pop()
                    for idx in range(4):
                        nx = ax + dx[idx]
                        ny = ay + dy[idx]
                        if nx >=0 and nx < m and ny >=0 and ny < n:
                            if graph[ny][nx] == 0:
                                graph[ny][nx] = 1
                                stack.append((ny,nx))
    return cnt
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
print(ice_juice(graph))