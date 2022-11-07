# 2022/11/06 baek 17140

R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
cnt = 0
row = len(arr)
col = len(arr[0])
while cnt <= 100:
  oper = ""
  if len(arr) >= R and len(arr[0]) >= C:
    if arr[R - 1][C - 1] == K:
      break

  if row >= col:
    oper = "R"
    # R 연산
    result = []
    max_length = 0

    for r in range(row):
      temp_list = []
      temp = [0] * 101

      for c in range(col):
        if arr[r][c] == 0:
          continue
        temp[arr[r][c]] += 1

      for i in range(1, 101):
        if temp[i] != 0:
          temp_list.append([i, temp[i]])
      temp_list.sort(key = lambda x : (x[1], x[0]))

      sub_result = []
      for sub in temp_list:
        sub_result += sub
      max_length = max(max_length, len(sub_result))
      result.append(sub_result)
      
  else:
    # C 연산
    oper = "C"
    result = []
    max_length = 0
    for c in range(col):
      temp_list = []
      temp = [0] * 101

      for r in range(row):
        if arr[r][c] == 0:
          continue
        temp[arr[r][c]] += 1

      for i in range(1, 101): 
        if temp[i] != 0:
          temp_list.append([i, temp[i]])
      temp_list.sort(key = lambda x : (x[1], x[0]))

      sub_result = []
      for sub in temp_list:
        sub_result += sub
      max_length = max(max_length, len(sub_result))
      result.append(sub_result)

  arr = [[0] * 101 for _ in range(101)]

  if oper == "R":
    for i in range(len(result)):
      if i == 100:
        break
      for j in range(len(result[i])):
        if j == 100:
          break
        arr[i][j] = result[i][j]

    col = min(max_length, 100)
  elif oper == "C":
    for i in range(len(result)):
      if i == 100:
        break
      for j in range(len(result[i])):
        if j == 100:
          break
        arr[j][i] = result[i][j]
    row = min(max_length, 100)
  cnt += 1

if cnt > 100:
  print(-1)
else:
  print(cnt)


# 파이썬의 장점을 살린 코드
from collections import Counter
def rc():
    max_len = 0
    len_s = len(s)
    for j in range(len_s):
        a = [i for i in s[j] if i != 0]
        a = Counter(a).most_common()
        a.sort(key = lambda x : (x[1], x[0]))
        s[j] = []
        for fi, se in a:
            s[j].append(fi)
            s[j].append(se)
        len_a = len(a)
        if max_len < len_a * 2: max_len = len_a * 2
    for j in range(len_s):
        for k in range(max_len - len(s[j])):
            s[j].append(0)
        s[j] = s[j][:100]
r, c, k = map(int, input().split())
s = [list(map(int, input().split())) for i in range(3)]
for i in range(101):
    try:
        if s[r - 1][c - 1] == k:
            print(i)
            break
    except: pass
    if len(s) < len(s[0]):
        s = list(zip(*s))
        rc()
        s = list(zip(*s))
    else:
        rc()
else:
    print(-1)