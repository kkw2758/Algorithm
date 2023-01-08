# 2023/01/08 Baek 3967

board = [list(input()) for _ in range(5)]
flag = 0
arr = []
check = [0] * 12

def dfs(depth, pos):
  global flag
  if depth == cnt:
    if (ord(board[0][4]) + ord(board[1][3]) + ord(board[2][2]) + ord(board[3][1]) - 4 * ord("A") + 4 != 26):
      return
    if (ord(board[0][4]) + ord(board[1][5]) + ord(board[2][6]) + ord(board[3][7]) - 4 * ord("A") + 4 != 26):
      return
    if (ord(board[1][1]) + ord(board[1][3]) + ord(board[1][5]) + ord(board[1][7]) - 4 * ord("A") + 4 != 26):
      return
    if (ord(board[1][1]) + ord(board[2][2]) + ord(board[3][3]) + ord(board[4][4]) - 4 * ord("A") + 4 != 26):
      return
    if (ord(board[1][7]) + ord(board[2][6]) + ord(board[3][5]) + ord(board[4][4]) - 4 * ord("A") + 4 != 26):
      return
    if (ord(board[3][1]) + ord(board[3][3]) + ord(board[3][5]) + ord(board[3][7]) - 4 * ord("A") + 4 != 26):
      return
    flag = 1
    return

  for i in range(12):
    if check[i]:
      continue
    check[i] = 1
    board[arr[pos][0]][arr[pos][1]] = chr(i + ord("A"))
    dfs(depth + 1, pos + 1)
    if flag:
      return
    board[arr[pos][0]][arr[pos][1]] = "x"
    check[i] = 0


cnt = 0
for i in range(5):
  for j in range(9):
    if "A" <= board[i][j] <= "L":
      check[ord(board[i][j]) - ord("A")] = 1
    if board[i][j] == "x":
      arr.append((i, j))
      cnt += 1

dfs(0, 0)
for i in board:
  print("".join(i))