# 2022/09/17 Baek 9663

# N = int(input())
# result = 0
# row = [0] * N

# def is_promising(x):
#   for i in range(x):
#     if row[i] == row[x] or abs(i - x) == abs(row[x] - row[i]):
#       return False
#   return True

# def n_queen(cnt):
#   global result
#   if cnt == N:
#     result += 1
#     return
#   for i in range(N):
#     row[cnt] = i
#     if is_promising(cnt):
#       n_queen(cnt + 1)

# n_queen(0)
# print(result)

N = int(input())

def is_promising(col, i):
  flag = True
  k = 0
  while (k < i and flag):
    if col[i] == col[k] or abs(col[i] - col[k]) == abs(i - k):
      flag = False
    k += 1
  return flag

def n_queens(col, i):
  if i == N:
    print(col)
    return
  else:
    for j in range(N):
      col[i] = j
      if is_promising(col, i):
        n_queens(col, i + 1)

col = [0] * N
n_queens(col, 0)