# 2022/12/13 baek 16933

import sys
from collections import deque

input = sys.stdin.readline

N, M, P = map(int, input().strip().split())
S = [0] + list(map(int, input().strip().split()))
board = []
for _ in range(N):
  board.append(list(input().strip()))

queues = [[]] + [deque() for _ in range(P)]
count = [0] * (P + 1)

for i in range(N):
  for j in range(M):
    if board[i][j] != "." and board[i][j] != "#":
      queues[int(board[i][j])].append((i, j))
      count[int(board[i][j])] += 1

def bfs():
  dx = [-1, 1, 0, 0]
  dy = [0 ,0, -1, 1]
  while True:
    flag = False
    for player in range(1, P + 1):
      if not queues[player]:
        continue
      q = queues[player]
      for round in range(S[player]):
        if not q:
          break
        for _ in range(len(q)):
          x, y = q.popleft()
          for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == ".":
              flag = True
              board[nx][ny] = str(player)
              count[player] += 1
              q.append((nx, ny))
            
    if flag == False:
      return 
        
bfs()

for i in count[1:]:
  print(i, end = " ")