# 해당 타일에 음식물이 있으면 1
# 해당 타일에 음식물이 없으면 0

def dfs(r, c):
    cnt = 0
    if r <= 0 or r > n or c <= 0 or c > m:
        return cnt

    if graph[r][c] == 1:
        cnt += 1
        graph[r][c] = 0
        
        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            cnt += dfs(nr, nc)    

    return cnt

import sys
sys.setrecursionlimit(100000)


n, m , k = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r][c] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


biggest_trash = 0


for r in range(1, n + 1):
    for c in range(1, m + 1):
        if graph[r][c] == 1:
            biggest_trash = max(dfs(r,c), biggest_trash)

print(biggest_trash)


#스택 풀이

def dfs_stack(r, c):
    stack = [[r, c]]
    cnt = 0
    while stack:
        r,c = stack.pop()
        
        if node[r][c]:
            node[r][c] = False
        else:
            continue

        if node[r + 1][c]:
            stack.append([r + 1, c])
        if node[r - 1][c]:
            stack.append([r - 1, c])
        if node[r][c - 1]:
            stack.append([r, c -1])
        if node[r][c + 1]:
            stack.append([r, c + 1])
        cnt += 1

    return cnt

n, m, k = map(int,input().split())
mx = 0
node = [[False] * (m + 2) for _ in range(n+2)]
for _ in range(k):
    r,c = map(int, input().split())
    node[r][c] = True

for i in range(1,n + 1):
    for j in range(1, m + 1):
        if node[i][j]:
            mx = max(mx,dfs_stack(i,j))

print(mx)
