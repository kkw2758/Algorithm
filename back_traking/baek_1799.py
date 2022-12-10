# # 2022/12/07 Baek 1799
# import sys
# input = sys.stdin.readline

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# result = 0

# def dfs(depth):
#   global result

#   result = max(result, depth)

#   for i in range(N):
#     for j in range(N):
#       if board[i][j] == 1:
#         board[i][j] = 2
#         if is_promising(i, j):
#           dfs(depth + 1)
#         board[i][j] = 1

# def is_promising(x, y):
#   dx = [-1, -1, 1, 1]
#   dy = [-1, 1, -1, 1]

#   for i in range(4):
#     for j in range(N):
#       nx = x + dx[i] * (j + 1)
#       ny = y + dy[i] * (j + 1)
#       if 0 <= nx < N and 0 <= ny < N:
#         if board[nx][ny] == 2:
#           return False

#   return True

# dfs(0)
# print(result)

import sys

# check : 현재 좌표 (x, y)에서 이전에 놓은 비숍에 영향을 받는지 아닌지를 체크하는 함수
def check(x, y):
    # 현재 칸이 비숍을 영향을 받으면 놓을 수 없으므로 False 리턴
    if temp[x][y]:
        return False
    # 그렇지 않다면 놓을 수 있으므로 True 리턴
    return True

# set : 현재 (x, y)에서 비숍을 놓거나 놓지 않는 함수. 이 때 num은 1 또는 -1로 놓는 경우는 1, 놓았다가 다시 빼는 경우는 -1로 나타낸다
def set(x,y,num):
    print(temp)
    for i in range(n):
        # 좌상 대각선
        nx, ny = x - i, y - i
        if 0 <= nx < n and 0 <= ny < n:
            temp[nx][ny] += num
        # 좌하 대각선
        nx, ny = x + i, y - i
        if 0 <= nx < n and 0 <= ny < n:
            temp[nx][ny] += num
        # 우상 대각선
        nx, ny = x - i, y + i
        if 0 <= nx < n and 0 <= ny < n:
            temp[nx][ny] += num
        # 우하 대각선
        nx, ny = x + i, y + i
        if 0 <= nx < n and 0 <= ny < n:
            temp[nx][ny] += num

# backtracking : 현재 idx번째 점에서 cnt개의 비숍을 놓는 함수
def backtracking(idx, cnt):
    global ans
    # Base Case : 모든 점을 탐색 후 정답 갱신
    if idx >= len(grid):
        ans = max(ans, cnt)
        return
    x, y = grid[idx]
    # 현재 칸에 놓을 수 있다면 backtracking
    if check(x, y):
        set(x, y, 1)
        backtracking(idx + 1, cnt + 1)
        set(x, y, -1)
        backtracking(idx + 1, cnt)
    # 놓을 수 없다면 다음 칸으로 이동
    else:
        backtracking(idx + 1, cnt)

# 입력부
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# temp : 비숍의 영향에 있는지 아닌지를 체크하는 2차원 배열, 0이면 영향에 있지 않고 1이면 영향에 있다
temp = [[0] * n for _ in range(n)]

# grid : 놓을 수 있는 좌표의 list
grid = []
ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            # 흰칸(검은칸)만 담음
            if (i + j) % 2 == 0:
                grid.append((i,j))
                
# 흰칸(검은칸)에 대해서만 백트래킹
backtracking(0,0)
res1 = ans

temp = [[0] * n for _ in range(n)]
grid = []
ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            # 검은칸(흰칸)만 담음
            if (i + j) % 2 == 1:
                grid.append((i,j))
                
# 검은칸(흰칸)에 대해서만 백트래킹
backtracking(0,0)
res2 = ans

# 두 경우를 더하여 정답 출력
print(res1 + res2)

n = int(input())

chess_map = []
black = []
white = []
color = [[0]*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    color[i][j] = (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)

for i in range(n):
  chess_map.append(list(map(int, input().split())))
  for j in range(n):
    if chess_map[i][j] == 1 and color[i][j] == 1:
      black.append((i, j))
    if chess_map[i][j] == 1 and color[i][j] == 0:
      white.append((i, j))

Bcnt = 0
Wcnt = 0

issued01 = [0] * (n * 2 - 1)
issued02 = [0] * (n * 2 - 1)

def fun(bishop, index, count):
  global Bcnt, Wcnt
  if index == len(bishop):
    rx, ry = bishop[index - 1]
    if color[rx][ry]:
      Bcnt = max(Bcnt, count)
    else:
      Wcnt = max(Wcnt, count)
    return

  x, y = bishop[index]
  if issued01[x + y] or issued02[x - y + n - 1]:
    fun(bishop, index + 1, count)
  else:
    issued01[x + y] = 1
    issued02[x - y + n - 1] = 1
    fun(bishop, index + 1, count + 1)
    issued01[x + y] = 0
    issued02[x - y + n - 1] = 0
    fun(bishop, index + 1, count)

if len(black) > 0:
  fun(black, 0, 0)
if len(white) > 0:
  fun(white, 0, 0)

print(Bcnt + Wcnt)