def dfs_stack(x, y):
    stack = []
    stack.append((x,y))
    cnt = 0

    while stack:
        x,y = stack.pop()
        if x < 0 or x > n -1 or y < 0 or y > n - 1:
            continue
        if graph[x][y] == 1:
            graph[x][y] = 0
            cnt += 1

            for idx in range(4):
                cnt += dfs_stack(x + dx[idx], y + dy[idx])

    return cnt

n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]





result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(dfs_stack(i,j))

result.sort()
print(len(result))
for x in result:
    print(x)



def dfs_recursive(x,y):
    cnt = 0
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return cnt
    if graph[x][y] == 0:
        return cnt
    else:
        # 방문 표시
        graph[x][y] = 0
        cnt += 1

        cnt += dfs_recursive(x, y - 1)
        cnt += dfs_recursive(x, y + 1)
        cnt += dfs_recursive(x - 1, y)
        cnt += dfs_recursive(x + 1, y)

    return cnt



n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(dfs_recursive(i,j))

result.sort()
print(len(result))
for x in result:
    print(x)
