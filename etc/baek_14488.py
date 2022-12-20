# 2022/12/19 Baek 14488

N, T = map(float, input().split())

student_info = []

pos = list(map(int, input().split()))
speed = list(map(int, input().split()))

for i in range(int(N)):
  left = round(pos[i] - speed[i] * T, 4)
  right = round(pos[i] + speed[i] * T, 4)
  student_info.append((left, right))

start, end = student_info[0]

flag = 1
for i in range(1, int(N)):
  if not(student_info[i][0] > end or student_info[i][1] < start):
    start = max(start, student_info[i][0])
    end = min(end, student_info[i][1])
  else:
    flag = 0
    break


print(flag)