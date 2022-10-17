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

# 인터넷을 참고한 정리된 코드
import sys
input = sys.stdin.readline

dr = [-1, 1, 0 ,0]
dc = [0, 0, -1, 1]

n  = int(input())
arr = [[0] * n for _ in range(n)]
students = []

for _ in range(n**2):
  students.append(list(map(int, input().split())))

for order in range(n**2):
  student = students[order]
  # 가능한 자리 저장
  tmp = []
  for i in range(n):
    for j in range(n):
      if arr[i][j] == 0:
        like = 0
        blank = 0
        for k in range(4):
          nr = i + dr[k]
          nc = j + dc[k]
          if 0 <= nr < n and 0 <= nc < n:
            if arr[nc][nr] in student[1:]:
              like += 1
            if arr[nc][nr] == 0:
              blank += 1
        tmp.append([like, blank, i, j])
  tmp.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
  arr[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
student.sort()

for i in range(n):
  for j in range(n):
    ans = 0
    for k in range(4):
      nr = i + dr[k]
      nc = j + dc[k]
      if 0 <= nr < n and 0 <= nc < n:
        if arr[nr][nc] in students[arr[i][j] - 1]:
          ans += 1

    if ans != 0:
      result += 10 ** (ans - 1)
      
print(result)