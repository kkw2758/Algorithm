# 2022/11/26 Baek 2457

def minus_one_day(date):
  day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  date = str(date)
  if len(date) == 3:
    if int(date[1:]) - 1 == 0:
      month = int(date[0]) - 1
      return int(str(month) + str(day_of_month[month]).zfill(2))
    else:
      return int(date[0] + str(int(date[1:]) - 1).zfill(2))
  elif len(date) == 4:
    if int(date[2:]) - 1 == 0:
      month = int(date[:2]) - 1
      return int(str(month) + str(day_of_month[month]).zfill(2))
    else:
      return int(date[:2] + str(int(date[2:]) - 1).zfill(2))

def plus_one_day(date):
  day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  date = str(date)
  if len(date) == 3:
    month = int(date[0])
    if int(date[1:]) + 1 > day_of_month[month]:
      month += 1
      return int(str(month) + "01")
    else:
      return int(str(month) + str(int(date[1:]) + 1).zfill(2))
  elif len(date) == 4:
    month = int(date[:2])
    if int(date[2:]) + 1 > day_of_month[month]:
      month += 1
      return int(str(month) + "01")
    else:
      return int(str(month) + str(int(date[2:]) + 1).zfill(2))

N = int(input())

flower_info = []
for _ in range(N):
  s_m, s_d, e_m, e_d = list(input().split())
  s = int(s_m.zfill(2) + s_d.zfill(2))
  e = int(e_m.zfill(2) + e_d.zfill(2))
  flower_info.append((s,e))


flower_info.sort()
start_period = 301
end_period = 1201


end = 0
for i in range(N):
  if flower_info[i][0] <= start_period:
    end = max(end, flower_info[i][1])
    
cnt = 1
while True:
  if end >= end_period:
    break
  flag = False
  temp = 0
  for i in range(N):
    if flower_info[i][0] <= end and flower_info[i][1] > end:
      temp = max(temp, flower_info[i][1])
      flag = True
  if flag == False:
    break
  end = temp
  cnt += 1

if end >= end_period:
  print(cnt)
else:
  print(0)