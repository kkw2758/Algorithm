# 복습
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
table = [ list(map(int, input().split())) for _ in range(m) ]
visited = [[0] * n for _ in range(m)]
directions = [(-1,0), (0,1), (1,0), (0,-1)]

count = 1
visited[x][y] = 1

while True:
    move = False
    for cnt in range(1,5):
        direction = (direction - 1)%4
        nx = x + directions[direction][0]
        ny = y + directions[direction][1]

        if table[nx][ny] == 1 or visited[nx][ny] == 1: # 바다이거나 방문했다면 
            continue
        
        move = True
        x = nx
        y = ny
        count += 1
        visited[x][y] = 1
        break

    if not move:
        nx = x - directions[direction][0]
        ny = y - directions[direction][1]
        if table[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny

print(count)

for row in table:
    print(row)
