# 2023/01/20 Baek 9207

N = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def backtracking(cnt):
  flag = False
  for x in range(5):
    for y in range(9):
      if board[x][y] == "o":
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if 0 <= nx < 5 and 0 <= ny < 9 and board[nx][ny] == "o":
            nnx = nx + dx[i]
            nny = ny + dy[i]
            if 0 <= nnx < 5 and 0 <= nny < 9 and board[nnx][nny] == ".":
              board[x][y] = "."
              board[nx][ny] = "."
              board[nnx][nny] = "o"
              flag = True
              backtracking(cnt + 1)
              board[x][y] = "o"
              board[nx][ny] = "o"
              board[nnx][nny] = "."
  if not flag:
    pin_cnt = 0
    for i in range(5):
      for j in range(9):
        if board[i][j] == "o":
          pin_cnt += 1
    candidates.append((pin_cnt, cnt))

cnt = 0
while True:
  cnt += 1
  board = [list(input()) for _ in range(5)]
  candidates = []
  backtracking(0)
  candidates.sort()
  print(candidates[0][0], candidates[0][1])
  if cnt == N:
    break
  input()