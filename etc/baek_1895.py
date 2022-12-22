# 2022/12/22 Baek 1895

R, C = map(int, input().split())

board = []
for _ in range(R):
  board.append(list(map(int, input().split())))

T = int(input())

filtered_value = []

for row in range(R - 2):
  for col in range(C - 2):
    temp = []
    for filter_row in range(row, row + 3):
      for filter_col in range(col, col + 3):
        temp.append(board[filter_row][filter_col])
    temp.sort(reverse=True)
    filtered_value.append(temp[len(temp) // 2])

cnt = 0
for i in range(len(filtered_value)):
  if filtered_value[i] >= T:
    cnt += 1

print(cnt)