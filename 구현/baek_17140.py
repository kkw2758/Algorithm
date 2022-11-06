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

# for _ in arr[:5]:
#   print(_[:5])