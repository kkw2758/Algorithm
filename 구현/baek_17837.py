# 2022/11/15 baek 17837

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

marker = [[[] for _ in range(N)] for _ in range(N)]
marker_info = []
for i in range(K):
  x, y, d = list(map(int, input().split()))
  marker[x - 1][y - 1].append(i)
  marker_info.append([x - 1, y - 1, d - 1])

def move(num):
  x, y, d = marker_info[num]
  nx = x + dx[d]
  ny = y + dy[d]

  if not(0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:

    if d % 2 == 0:
      d += 1
    else:
      d -= 1

    marker_info[num][2] = d
    nx = x + dx[d]
    ny = y + dy[d]
    if not(0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:
      return True

  numbers = []

  for i in range(len(marker[x][y])):
    if marker[x][y][i] == num:
      numbers += marker[x][y][i:]
      marker[x][y] = marker[x][y][:i]
      break

  if board[nx][ny] == 1:
    numbers.reverse()

  marker[nx][ny] += numbers
  for number in numbers:
    marker_info[number][0], marker_info[number][1] = nx, ny 
  if len(marker[nx][ny]) >= 4:
    return False
  return True
  

turn = 0
while True:
  flag = False
  turn += 1
  for i in range(K):
    if not(move(i)):
      flag = True
      break
  if flag:
    print(turn)
    break
  if turn > 1000:
    print(-1)
    break  