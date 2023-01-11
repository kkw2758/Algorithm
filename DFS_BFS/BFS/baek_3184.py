# 2023/01/11 Baek 3184

R, C = map(int, input().split())
board = []
wolf = []
sheep = []
for i in range(R):
  board.append(list(input().strip()))
  for j in range(C):
    if board[i][j] == "v":
      wolf.append((i, j))
    if board[i][j] == "o":
      sheep.append((i, j))

visited = [[False] * C for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  stack = [(x, y)]
  visited[x][y] = True
  
  sheep_cnt = 0
  wolf_cnt = 0

  if board[x][y] == "v":
    wolf_cnt += 1
  
  if board[x][y] == "o":
    sheep_cnt += 1

  while stack:
    x, y = stack.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
        if board[nx][ny] == "#":
          continue
        else:
          visited[nx][ny] = True
          stack.append((nx, ny))
          if board[nx][ny] == "v":
            wolf_cnt += 1
          
          if board[nx][ny] == "o":
            sheep_cnt += 1

  if sheep_cnt > wolf_cnt:
    wolf_cnt = 0
  else:
    sheep_cnt = 0
  return sheep_cnt, wolf_cnt

sheep_cnt = 0
wolf_cnt = 0

for x, y in sheep:
  if not visited[x][y]:
    result = dfs(x, y)
    sheep_cnt += result[0]
    wolf_cnt += result[1]

for x, y in wolf:
  if not visited[x][y]:
    result = dfs(x, y)
    sheep_cnt += result[0]
    wolf_cnt += result[1]

print(sheep_cnt, wolf_cnt)