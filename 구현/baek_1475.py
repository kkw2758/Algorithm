# 2023/02/03 Baek 1475

N = input()
number_cnt = [0]*10

for i in range(len(N)):
  if int(N[i]) == 6 or int(N[i]) == 9:
    if number_cnt[6] > number_cnt[9]:
      number_cnt[9] += 1
    else:
      number_cnt[6] += 1
  else:
    number_cnt[int(N[i])] += 1

print(max(number_cnt))