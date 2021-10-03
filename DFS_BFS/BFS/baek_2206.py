# 참고링크 : https://pacific-ocean.tistory.com/348
import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


# visit[x][y][w] 라고할때 w 값이 1이면 벽을 안깬상태, w 값이 0이면 이미 벽을 깬 상태
def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    visit = [[[0]*2 for i in range(m)] for j in range(n)]
    visit[0][0][1] = 1 # 시작지점 방문처리

    while queue:
        x, y, w = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][w]

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < m:
                # 만약 다음 방문지점이 벽이고 아직 벽을 깨지 않았다면
                # 벽을 꺠는 과정에서 다음지점의 방문 여부를 검사하지 않는 이유 - 벽을깨는순간 w = 0으로 전환되므로 똑같은곳에서 여러번 벽을 깰 필요가 없다.
                if board[nx][ny] == 1 and w == 1:
                    visit[nx][ny][0] = visit[x][y][w] + 1
                    queue.append([nx,ny,0])
                # 만약 다음 방문지점이 벽이아니고 아직 방문하지 않았다면
                # visit[nx][ny][w] == 0 을 검사하는이유
                # 만약 이미 방문했더라면 이미 이전에 방문했다는 뜻 즉, 더빠른 경로가 존재한다!
                elif board[nx][ny] == 0 and visit[nx][ny][w] == 0:
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    queue.append([nx, ny, w])
    
    return -1


n, m = map(int, input().split())
board = [list(map(int, list(input().strip()))) for row in range(n)]
print(bfs())

# 복습
import sys
from collections import deque
n, m = map(int, input().split())
table = []

input = sys.stdin.readline

for _ in range(n):
    table.append(list(map(int, list(input().strip()))))

def bfs_1():
    visited = [[[0,0] for i in range(m)] for j in range(n)]
    visited[0][0][1] = 1

    queue = deque()
    queue.append((0,0,1))
    dx = [-1, 1, 0, 0]
    dy = [0, 0 , -1 , 1]

    while queue:
        x, y, w = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            if w == 1 and table[nx][ny] == 1:
                visited[nx][ny][0] = visited[x][y][w] + 1
                queue.append((nx, ny, 0))

            elif visited[nx][ny][w] == 0 and table[nx][ny] == 0:
                visited[nx][ny][w] = visited[x][y][w] + 1
                queue.append((nx, ny, w))
    return -1

print(bfs_1())

'''
# 나의 오답 코드
# 벽을 깬여부를 추가한것 까진 좋았지만 방문처리를 제대로 해줄 방법을 생각하지 못했다..
from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0,0,0))
    level = 1
    board[0][0] = 2
    while queue:
        queue_size = len(queue)
        for _ in range(queue_size):
            x, y, flag = queue.popleft()
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if nx == n - 1 and ny == m - 1:
                    return level + 1
                #만약 벽이라면 board[nx][ny] == 1
                if board[nx][ny] == 1:
                    if flag == 0:   # 벽을 파괴할 수 있다면
                        board[nx][ny] = 2
                        queue.append((nx, ny, 1))
                #만약 벽이아니라면 board[nx][ny] == 0
                elif board[nx][ny] == 0:
                    board[nx][ny] = 2
                    queue.append((nx, ny, flag))

        level += 1
    
    return -1

                
n, m = map(int, input().split())
board = [list(map(int, list(input().strip()))) for row in range(n)]

print(bfs())
'''