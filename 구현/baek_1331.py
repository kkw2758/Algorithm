# # 2023/01/16 Baek 1331

# board = [[False] * 6 for _ in range(6)]
# indexes = []
# for _ in range(36):
#   index = input()
#   x = ord(index[0]) - ord("A")
#   y = int(index[1]) - 1
#   indexes.append((x, y))

# def check():
#   for x, y in indexes:
#     if not board[x][y]:
#       board[x][y] = True
#     else:
#       return "Invalid"
  
#   return "Valid"

# print(check())

# for _ in board:
#   print(_)


d = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
visited = [[0] * 6 for _ in range(6)]
indexes = []
for i in range(36):
  index = input()
  x = ord(index[0]) - ord("A")
  y = int(index[1]) - 1
  indexes.append((x, y))


x, y = indexes[0][0], indexes[0][1]
ex, ey = indexes[-1][0], indexes[-1][1]
if [ex - x, ey - y] not in d:
  print("Invalid")
else:
  visited[x][y] = 1
  for nx, ny in indexes[1:]:
    if [nx - x, ny - y] not in d or visited[nx][ny] != 0:
      print("Invalid")
      break
    visited[nx][ny] += 1
    x, y = nx, ny
  else:
    print("Valid")