#2022/10/16 baek 21608

import sys
input = sys.stdin.readline

n = int(input())
table = [[0] * (n + 1) for _ in range(n + 1)]
students = []

for _ in range(n * n):
  students.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for student in students:
  first_case = [[], [], [], [], []]
  for x in range(1, n + 1):
    for y in range(1, n + 1):
      if table[x][y] == 0:
        cnt = 0
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if 1 <= nx <= n and 1 <= ny <= n:
            if table[nx][ny] in student[1:]:
              cnt += 1

        first_case[cnt].append((x,y))

  for i in range(4, -1, -1):
    if len(first_case[i]) == 1:
      table[first_case[i][0][0]][first_case[i][0][1]] = student[0]
      # print("first")
      # for _ in table:
      #   print(_)
      # print()
      break
    elif len(first_case[i]) > 1:
      second_case = [[], [], [], [], []]
      for x, y in first_case[i]:
        cnt = 0
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if 1 <= nx <= n and 1 <= ny <= n:
            if table[nx][ny] == 0:
              cnt += 1
        second_case[cnt].append((x,y))  #second_case 다만듬

      for i in range(4, -1, -1):
        if len(second_case[i]) >= 1:
          table[second_case[i][0][0]][second_case[i][0][1]] = student[0]
          # print("second or third")
          # for _ in table:
          #   print(_)
          # print()
          break
      break

students.sort()
result = 0
score = [0, 1, 10, 100, 1000]
for x in range(1, n + 1):
  for y in range(1, n + 1):
    cnt = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 1 <= nx <= n and 1 <= ny <= n:
        if table[nx][ny] in students[table[x][y] - 1][1:]:
          cnt += 1
    result += score[cnt]

print(result)