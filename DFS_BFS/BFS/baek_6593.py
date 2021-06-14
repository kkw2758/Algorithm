import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_x, start_y, start_z):
    queue = deque()
    queue.append((start_x, start_y, start_z))
    building[start_x][start_y][start_z] = "#"
    minute = 0
    while queue:
        queue_size = len(queue)
        for _ in range(queue_size):
            x, y, z = queue.popleft()

            for idx in range(6):
                nx = x + dx[idx]
                ny = y + dy[idx]
                nz = z + dz[idx]

                if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                    if building[nx][ny][nz] != "#":
                        if building[nx][ny][nz] == "E":
                            return "Escaped in {} minute(s).".format(minute + 1)
                        queue.append((nx, ny, nz))
                        building[nx][ny][nz] = "#"

        minute += 1

    return "Trapped!"

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 0, 1, 0, -1]
dz = [0, 0, -1, 0, 1, 0]

while True:
    L, R, C = map(int, input().split())
    
    if L == 0 and R == 0 and C == 0 :
        break

    building = []
    
    #빌딩정보 입력받음
    for height in range(L):
        matrix = []
        for row in range(R):
            tmp = list(input().strip())
            if "S" in tmp:
                #S의 좌표 = (start_x, start_y, start_z)
                start_x = height
                start_y = row
                start_z = tmp.index("S")

            matrix.append(tmp)
        input()
            
        building.append(matrix)

    print(bfs(start_x, start_y, start_z))