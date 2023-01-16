# 2023/01/16 Baek 1331

board = [[False] * 6 for _ in range(6)]
indexes = []
for _ in range(36):
  index = input()
  x = ord(index[0]) - ord("A")
  y = int(index[1]) - 1
  indexes.append((x, y))

def check():
  for x, y in indexes:
    if not board[x][y]:
      board[x][y] = True
    else:
      return "Invalid"
  
  return "Valid"

print(check())

for _ in board:
  print(_)