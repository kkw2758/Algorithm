# 2023/01/19 Baek 2784
words = []

for i in range(6):
  words.append(input())

board = []
visited = [False] * 6

flag = False
def check_board():
  not_visited = []
  for i in range(6):
    if visited[i] == False:
      not_visited.append(words[i])
  not_visited.sort()
  columns = []

  for i in range(3):
    columns.append(board[0][i] + board[1][i] + board[2][i])
  columns.sort()

  if not_visited == columns:
    return True
  else:
    return False   


def backtraking(depth):
  global flag
  if depth == 3:
    if check_board():
      flag = True
      return

  for i in range(6):
    if not visited[i]:
      visited[i] = True
      board.append(words[i])
      backtraking(depth + 1)
      if flag:
        break
      board.pop()
      visited[i] = False

backtraking(0)

if not flag:
  print(0)
else:
  for _ in board:
    print(_)