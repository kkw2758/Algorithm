'''
기존 자표 x, y
L : x, y - 1
R : x, y + 1
U : x - 1, y
D : x + 1, y
'''

#나의풀이
#딕셔너리를 이용해서 이동위치에 따른 좌표이동값을 매칭시켜서 구현
direction = { 'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}
n = int(input())
plan = input().split()

x, y = 1, 1 #시작점 좌표

for way in plan:
    x += direction[way][0]
    y += direction[way][1]

    if x == 0 or x == n + 1 or y == 0 or y == n + 1:
        x -= direction[way][0]
        y -= direction[way][1]

print(x, y)


#답지풀이
#리스트 3개를 생성해서 이동위치, 이동위치에 따른(x,y) 좌표 이동값을 저장 
n = int(input())
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
x, y = 1, 1

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x,y = nx, ny


print(x, y)