import sys
sys.setrecursionlimit(1000000)

def dfs_recursive(x, y, h):
    # 지금 구간이 물에 잠기는지 체크
    if matrix[x][y] <= h:
        return False

    #방문 체크
    visit[x][y] = 1

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
    
        if not visit[nx][ny]:
            dfs_recursive(nx, ny, h)

    return True


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

#해당구역 방문여부를 기록할 리스트
#visit = [[0]*n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = 0

for h in range(101):
    visit = [[0]*n for _ in range(n)]
    tmp = 0
    for i in range(n):

        for j in range(n):
            if matrix[i][j] > h and not(visit[i][j]):
                dfs_recursive(i, j, h)
                tmp += 1
    print("h = {}".format(h))
    for _ in visit:
        print(_)
    print("result = {}".format(tmp))
    if tmp == 0:
        break
    result = max(result,tmp)

print(result)