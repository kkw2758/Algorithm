# 2023/01/20 Baek 3085
import sys

N = int(input())
dx = [0, 1]
dy = [1, 0]

board = [list(input()) for _ in range(N)]

result = 0

def check(ary):
  before = ary[0]
  cnt = 1
  result = 0
  for i in range(1, N):
    if before == ary[i]:
      cnt += 1
    else:
      result = max(result, cnt)
      cnt = 1
      before = ary[i]
  result = max(result, cnt)
  return result

for x in range(N):
  for y in range(N):
    for i in range(2):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        if board[x][y] != board[nx][ny]:
          board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
          for j in range(N):
            result = max(result, check(board[j]))
            temp = []
            for k in range(N):
              temp.append(board[k][j])
            result = max(result, check(temp))
            if result == N:
              print(N)
              sys.exit()
          board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
        
print(result)