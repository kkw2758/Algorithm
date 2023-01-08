# 2022/12/26 baek 16235

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
board = [[5] * N for _ in range(N)]
trees = []

for _ in range(M):
  trees.append(list(map(int, input().split())))

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(K):
  # spring
  trees.sort(key = lambda x : x[2])
  dead_trees = []
  idx = 0
  for _ in range(len(trees)):
    r, c, age = trees[idx]
    if age > board[r - 1][c - 1]:
      dead_trees.append(trees.pop(idx))
    else:
      trees[idx][2] += 1
      board[r - 1][c - 1] -= age
      idx += 1

  # summer
  for _ in range(len(dead_trees)):
    r, c, age = dead_trees.pop()
    board[r - 1][c - 1] += age // 2

  # autumn
  for tree in trees:
    r, c, age = tree
    if age % 5 != 0:
      continue
    r = r - 1
    c = c - 1
    for idx in range(8):
      nr = r + dr[idx]
      nc = c + dc[idx]
      if 0 <= nr < N and 0 <= nc < N:
        trees.append([nr + 1, nc + 1, 1])

  # winter
  for r in range(N):
    for c in range(N):
      board[r][c] += A[r][c]


print(len(trees))