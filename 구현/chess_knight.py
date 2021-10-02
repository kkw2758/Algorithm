y_list = [chr(x + 97) for x in range(0,8)]

start_point = input()
x = int(start_point[1])
y = ord(start_point[0]) - ord('a') + 1
count = 0

move_types = [(-2,-1), (-1,-2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2,1)]
for direction in move_types:
    nx = x + direction[0]
    ny = y + direction[1]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    
    count += 1

print(count)


# 복습
start_point = input()
x = ord(start_point[0]) - 96
y = int(start_point[1])
count = 0

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1 ,1]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count += 1

print(count)