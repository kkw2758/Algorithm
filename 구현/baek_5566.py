# 2023/01/19 Baek 5566

N, M = map(int, input().split())
board = []
for _ in range(N):
  board.append(int(input()))

idx = 0
for i in range(M):
  dice_number = int(input())
  next_idx = idx + dice_number
  if next_idx >= N - 1:
    print(i + 1)
    break
  next_idx += board[next_idx]
  if next_idx >= N - 1:
    print(i + 1)
    break
  idx  = next_idx
