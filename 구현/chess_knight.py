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