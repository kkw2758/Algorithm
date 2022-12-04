# 2022/12/01 Baek 1170

N, K = map(int, input().split())
schedule = list(map(int, input().split()))
multitab = []
cnt = 0
for i in range(K):
  if schedule[i] in multitab:
    continue

  if len(multitab) < N:
    multitab.append(schedule[i])
  else: # 꽂을 자리가 없으면
    temp = []
    for plug in multitab:
      flag = False
      for j in range(i + 1, K):
        if schedule[j] == plug:
          temp.append([plug, j])
          flag = True
          break
      if flag == False:
        temp.append([plug, 101])
    temp.sort(key = lambda x : x[1])
    multitab = [x[0] for x in temp[:-1]]
    multitab.append(schedule[i])
    cnt += 1
  # print(i, multitab)

print(cnt)