# 2023/01/14 Baek 1347

N = int(input())
move = input()

# 남 동 북 서 왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
indexes = [[0, 0]]
d = 0

x, y = 0, 0
for i in move:
  if i == "R":
    d = (d - 1) % 4
  elif i == "L":
    d = (d + 1) % 4
  elif i == "F":
    x = x + dx[d]
    y = y + dy[d]
    indexes.append([x, y])

min_x = 51
min_y = 51
max_x = 0
max_y = 0
for x, y in indexes:
  min_x = min(min_x, x)
  max_x = max(max_x, x)
  min_y = min(min_y, y)
  max_y = max(max_y, y)

result = [["#"] * (abs(max_y - min_y) + 1) for _ in range(abs(max_x - min_x) + 1)]

for x, y in indexes:
  result[x - min_x][y - min_y] = "."

for row in result:
  print("".join(row))