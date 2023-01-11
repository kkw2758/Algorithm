# 2023/01/11 Baek 13901

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
k = int(input())

board = [["*"]  * C for _ in range(R)]

for _ in range(k):
  x, y = map(int, input().split())
  board[x][y] = "x"

sr, sc = map(int, input().split())

direction = list(map(int, input().split()))
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

stack = []
stack.append((sr, sc))
board[sr][sc] = 0
d = 0

while True:
  x, y = stack.pop()
  flag = False
  for i in range(4):
    nx = x + dx[direction[d]]
    ny = y + dy[direction[d]]
    if not(0 <= nx < R and 0 <= ny < C):
      d = (d + 1) % 4
      continue
    if board[nx][ny] != "*":
      d = (d + 1) % 4
      continue
    
    board[nx][ny] = board[x][y] + 1
    stack.append((nx, ny))
    flag = True
    break

  if not flag:
    print(x, y)
    break


# 인터넷 참고 풀이
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
k = int(input())
lst = [[0] * m for _ in range(n)]

for i in range(k):
  x, y = map(int, input().split())
  lst[x][y] = 1

sr, sc = map(int, input().split())
lst[sr][sc] = 1

move = list(map(int, input().split()))