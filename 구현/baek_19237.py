# n, m, k = map(int, input().split())
# #냄새 뿌린 상어 번호, 방향, 냄새 사라지는 시간
# table = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
# result = 0

# temp = []
# for i in range(n):
#   temp.append(list(map(int, input().split())))

# directions = list(map(int, input().split()))

# direction_idx = 0
# for i in range(n):
#   for j in range(n):
#     if temp[i][j] != 0:
#       table[i][j][0] = temp[i][j]
#       table[i][j][2] = k
#       # table[i][j][1] = directions[direction_idx] - 1
#       table[i][j][1] = directions[direction_idx]
#       direction_idx += 1

# # for _ in table:
# #   print(_)
# #초기 설정 완료

# def find_all_sharks():
#   sharks = []
#   for i in range(n):
#     for j in range(n):
#       #상어가 냄새뿌린 자리에 있을 때 좌표를 리턴
#       if table[i][j][1] != 0 and table[i][j][2] == k:
#         sharks.append((table[i][j][0], i, j))
#   return sharks

# # sharks = find_all_sharks()
# # print(sharks)

# #위, 아래, 왼쪽, 오른쪽
# dx = [False, -1, 1, 0, 0]
# dy = [False, 0, 0, -1, 1]

# priority = [[] for _ in range(m)]

# for i in range(m):
#   for j in range(4):
#     priority[i].append(list(map(int, input().split())))


# def find_direction(shark_number, x, y):
#   before_direction = 100
#   now_direction = table[x][y][1]
#   for i in priority[shark_number-1][now_direction - 1]:
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0 <= nx < n and 0 <= ny < n:
#       #이전의 방향 저장
#       if shark_number == table[nx][ny][0] and table[nx][ny][2] == k-1:
#         before_direction = i
#         # print(before_direction)
#       #냄새가 없으면
#       if table[nx][ny][2] == 0:
#         return i
#   return before_direction

# def smell_down():
#   for i in range(n):
#     for j in range(n):
#       if table[i][j][1] == 0:
#         if table[i][j][2] == 0:
#           continue
#         if table[i][j][2] == 1:
#           table[i][j] = [0, 0, 0]
#         else:
#           table[i][j][2] -= 1
#           # table[i][j][1] = 0
          
                

# #sharks > [(1, 0, 0), (2, 3, 3)]
# #상어 번호 x, y
# def move_sharks():
#   count = 0
#   global result
#   while True:
#     if count == 23:
#       return
#     count += 1
#     for _ in table:
#       print(_)
#     print("="* 20)
#     sharks = find_all_sharks()
#     # print(sharks)
#     if len(sharks) == 1:
#       print("끝")
#       return
#     new_sharks = []
#     for shark in sharks:
#       shark_number = shark[0]
#       x, y = shark[1], shark[2]
#       # print(shark)
#       direction = find_direction(shark_number, x, y)
#       # print("direction = {}".format(direction))
#       nx = x + dx[direction]
#       ny = y + dy[direction]

#       new_sharks.append((shark_number, direction, nx, ny, x, y))

#       # if 0 < table[nx][ny][0] < shark_number:
#       #   continue
#       # table[nx][ny] = [shark_number, direction, k]
#       # table[x][y][1] = 0

#     for new_shark in new_sharks:
#       new_shark_number = new_shark[0]
#       new_shark_direction = new_shark[1]
#       nx = new_shark[2]
#       ny = new_shark[3]
#       before_x = new_shark[4]
#       before_y = new_shark[5]

#       table[before_x][before_y][1] = 0
#       if table[nx][ny][0] == 0 or table[nx][ny][0] > new_shark_number or table[nx][ny][0] == new_shark_number:
#         table[nx][ny] = [new_shark_number, new_shark_direction, k]
#         continue
      
#     smell_down()  
#     result += 1

# move_sharks()
# print(result)


'''
4 2 6
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 2
4 3
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3
'''

n, m, k = map(int, input().split())

array = []
for i in range(n):
  array.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

smell = [[[0,0]] * n for _ in range(n)]

priorities = [[] for _ in range(m)]
for i in range(m):
  for j in range(4):
    priorities[i].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(smell)

def update_smell():
  for i in range(n):
    for j in range(n):
      if smell[i][j][1] > 0:
        smell[i][j][1] -= 1
      if array[i][j] != 0:
        smell[i][j] = [array[i][j], k]

def move():
  new_array = [[0] * n for _ in range(n)]
  for x in range(n):
    for y in range(n):
      if array[x][y] != 0:
        direction = directions[array[x][y] - 1]
        found = False
        for index in range(4):
          nx = x + dx[priorities[array[x][y] - 1][direction -1][index] - 1]
          ny = y + dy[priorities[array[x][y] - 1][direction -1][index] - 1]
          if 0 <= nx < n and 0 <= ny < n:
            if smell[nx][ny][1] == 0:
              directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]

              if new_array[nx][ny] == 0:
                new_array[nx][ny] = array[x][y]
              else:
                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
              found = True
              break
          
        if found:
          continue

        for index in range(4):
          nx = x + dx[priorities[array[x][y] - 1][direction -1][index] - 1]
          ny = y + dy[priorities[array[x][y] - 1][direction -1][index] - 1]
          if 0 <= nx < n and 0 <= ny < n:
            if smell[nx][ny][0] == array[x][y]:
              directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
              new_array[nx][ny] = array[x][y]
              break
  return new_array

time = 0
while True:
  update_smell()
  new_array = move()
  array = new_array
  time += 1

  check = True
  for i in range(n):
    for j in range(n):
      if array[i][j] > 1:
        check = False
  if check:
    print(time)
    break

  if time >= 1000:
    print(-1)
    break