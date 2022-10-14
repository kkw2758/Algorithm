# # 2022/10/11 baek 18808

# def rotate_90(arr):
#   row = len(arr)
#   col = len(arr[0])
#   result = [[0] * row for _ in range(col)]
#   for r in range(row):
#     for c in range(col):
#       result[c][row  - 1 - r] = arr[r][c]
  
#   return result

# def check(arr):
#   for r in range(len(arr)):
#     for c in range(len(arr[0])):
#       if arr[r][c] == 2:
#         return False
#   return True

# def put_sticker(sticker):
#     row = len(sticker)
#     col = len(sticker[0])

#     if n < row or m < col:
#       return False

#     for start_r in range(n - row + 1):
#       for start_c in range(m - col + 1):
#         for r in range(row):
#           for c in range(col):
#             notebook[start_r + r][start_c + c] += sticker[r][c]
#         if check(notebook):
#           return True
#         else:
#           for r in range(row):
#             for c in range(col):
#               notebook[start_r + r][start_c + c] -= sticker[r][c]
#     return False

# n, m, k = map(int, input().split())
# notebook = [[0] * m for _ in range(n)]
# stickers = []

# for _ in range(k):
#   r, c = map(int, input().split())
#   sticker = []

#   for _ in range(r):
#     sticker.append(list(map(int, input().split())))

#   stickers.append(sticker)

# for sticker in stickers:
#   if put_sticker(sticker):
#     print("sticker", sticker)
#     for _ in notebook:
#       print(_)
#     print()
#     continue
#   else:
#     for i in range(3):  # 4 방향 검사
#       sticker = rotate_90(sticker)
#       if put_sticker(sticker):
#         print(i,"sticker", sticker)
#         for _ in notebook:
#           print(_)
#         print()
#         break

# 2022/10/11 baek 18808
import sys
input = sys.stdin.readline

def rotate_90(arr):
  row = len(arr)
  col = len(arr[0])
  result = [[0] * row for _ in range(col)]
  for r in range(row):
    for c in range(col):
      result[c][row  - 1 - r] = arr[r][c]
  
  return result

def check(arr):
  for r in range(len(arr)):
    for c in range(len(arr[0])):
      if arr[r][c] == 2:
        return False
  return True

def put_sticker(sticker):
    row = len(sticker)
    col = len(sticker[0])

    if n < row or m < col:
      return False

    for start_r in range(n - row + 1):
      for start_c in range(m - col + 1):
        for r in range(row):
          for c in range(col):
            notebook[start_r + r][start_c + c] += sticker[r][c]
        if check(notebook):
          return True
        else:
          for r in range(row):
            for c in range(col):
              notebook[start_r + r][start_c + c] -= sticker[r][c]
    return False

n, m, k = map(int, input().split())
notebook = [[0] * m for _ in range(n)]
stickers = []

for _ in range(k):
  r, c = map(int, input().split())
  sticker = []

  for _ in range(r):
    sticker.append(list(map(int, input().split())))

  stickers.append(sticker)

for sticker in stickers:
  if put_sticker(sticker):
    continue
  else:
    for i in range(3):  # 4 방향 검사
      sticker = rotate_90(sticker)
      if put_sticker(sticker):
        break

cnt = 0
for i in range(len(notebook)):
  for j in range(len(notebook[0])):
    if notebook[i][j] == 1:
      cnt += 1

print(cnt)