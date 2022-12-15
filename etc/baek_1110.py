# 2022/12/15 Baek 1110

N = int(input())

cnt = 0
temp = N
while True:
  print(temp)
  if temp < 10:
    temp = int(str(temp) * 2)
  else:
    temp = int(str(temp % 10) + str(temp // 10 + temp % 10)[-1])
  cnt += 1
  if temp == N:
    break
  

print(cnt)