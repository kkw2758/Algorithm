# 2022/09/16 Baek 9251

first = input()
second = input()

table = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

for row in range(1, len(first) + 1):
  for col in range(1, len(second) + 1):
    if first[row - 1] == second[col - 1]:
      table[row][col] = table[row - 1][col - 1] + 1
    else:
      table[row][col] = max(table[row - 1][col], table[row][col - 1])

print(table[-1][-1])


first = input()
second = input()

table = [0] * len(second)
for i in range(len(first)):
  cnt = 0
  for j in range(len(second)):
    if cnt < table[j]:
      cnt = table[j]
    elif first[i] == second[j]:
      table[j] = cnt + 1

print(max(table))