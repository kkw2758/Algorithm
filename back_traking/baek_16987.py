# 2022/12/04 Baek 16987

import sys
input = sys.stdin.readline

N = int(input())
egg_info = []
for i in range(N):
  egg_info.append(list(map(int, input().split())))

result = 0

def dfs(egg_idx):
  global result

  if egg_idx == N:
    cnt = 0
    for i in egg_info:
      if i[0] <= 0:
        cnt += 1
    result = max(result, cnt)
    return

  # 가지고 있는 계란이 깨졌으면
  if egg_info[egg_idx][0] <= 0:
    dfs(egg_idx + 1)
  else:
    flag = True
    for i in range(N):
      if egg_idx != i and egg_info[i][0] > 0:
        flag = False
        egg_info[egg_idx][0] -= egg_info[i][1]
        egg_info[i][0] -= egg_info[egg_idx][1]
        dfs(egg_idx + 1)
        egg_info[egg_idx][0] += egg_info[i][1]
        egg_info[i][0] += egg_info[egg_idx][1]
      
    if flag:
      dfs(N)

dfs(0)
print(result)


# 2022/12/04 Baek 16987

N = int(input())
egg_info = []
for i in range(N):
  egg_info.append(list(map(int, input().split())))

result = 0
def dfs(egg_idx, cnt):
  global result
  if egg_idx == N:
    result = max(result, cnt)
    return
  else:
    if egg_info[egg_idx][0] <= 0:
      dfs(egg_idx + 1, cnt)
    else:
      flag = True
      for i in range(N):
        if egg_idx != i and egg_info[i][0] > 0:
          flag = False
          egg_info[egg_idx][0] -= egg_info[i][1]
          egg_info[i][0] -= egg_info[egg_idx][1]

          if egg_info[egg_idx][0] <= 0 and egg_info[i][0] <= 0: 
            dfs(egg_idx + 1, cnt + 2)
          elif egg_info[egg_idx][0] <= 0 or egg_info[i][0] <= 0:
            dfs(egg_idx + 1, cnt + 1)
          else:
            dfs(egg_idx + 1, cnt)

          egg_info[egg_idx][0] += egg_info[i][1]
          egg_info[i][0] += egg_info[egg_idx][1]
      if flag:
        dfs(N, cnt)

dfs(0, 0)
print(result)