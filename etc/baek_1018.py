N, M = map(int, input().split())

board = []

for _ in range(N):
  board.append(list(input()))

def check_board(board):
  patterns = [["W", "B", "W", "B", "W", "B", "W", "B"], ["B", "W", "B", "W", "B", "W", "B", "W"]]
  if board[0] == patterns[0]:
    idx = 0
  elif board[0] == patterns[1]:
    idx = 1
  else:
    return False

  for i in range(8):
    if board[i] != patterns[idx]:
      return False
    idx = (idx + 1) % 2

  return True

cnt = 0
for i in range(N - 8 + 1):
  for j in range(M - 8 + 1):
    temp_board = []
    for k in range(i, i + 8):
      temp_board.append(board[k][j:j + 8])
    if not check_board(temp_board):
      cnt += 1

print(cnt)