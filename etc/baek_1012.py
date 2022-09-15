# 2022/09/15 Baek 1012

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recursive_dfs(start_x, start_y):
  ary[start_x][start_y] = 0
  for idx in range(4):
    nx = start_x + dx[idx]
    ny = start_y + dy[idx]
    if 0 <= nx < N and 0 <= ny < M:
      if ary[nx][ny] == 1:
        ary[nx][ny] = 0
        recursive_dfs(nx, ny)

# def dfs(start_x, start_y):
#   stack = [(start_x, start_y)]
#   ary[start_x][start_y] = 0
#   while stack:
#     x, y = stack.pop()
#     for idx in range(4):
#       nx = x + dx[idx]
#       ny = y + dy[idx]
#       if 0 <= nx < N and 0 <= ny < M:
#         if ary[nx][ny] == 1:
#           ary[nx][ny] = 0
#           stack.append((nx, ny))

T = int(input())
for _ in range(T):
  # 가로 세로 배추 개수
  M, N, K = map(int, input().split())
  ary = [[0] * M for _ in range(N)]

  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  for _ in range(K):
    x, y = map(int, input().split())
    ary[y][x] = 1

  result = 0
  for row in range(N):
    for col in range(M):
      if ary[row][col] == 1:
        recursive_dfs(row, col)
        result += 1
  print(result)
