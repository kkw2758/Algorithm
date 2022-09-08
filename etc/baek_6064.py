# 2022/09/08 Baek 6064
# T = int(input())
# for _ in range(T):
#   M, N, x, y = map(int, input().split())
#   result = -1
#   circulation = set()
#   temp = x % N
#   if temp == 0:
#     temp = N
#   if temp == y:
#     print(x)
#     continue
#   circulation.add(temp)
#   while True:
#     x = x + M
#     temp = x % N
#     if temp == 0:
#       temp = N

#     if temp == y:
#       result = x
#       break
#     if temp in circulation:
#       break
#     else:
#       circulation.add(temp)

#   print(result)



T = int(input())
for _ in range(T):
  M, N, x, y = map(int, input().split())
  result = -1
  circulation = set()
  cnt = 0
  while True:
    temp_x = x + M * cnt
    temp_y = N if temp_x % N == 0 else temp_x % N
    if temp_y == y:
      result = temp_x
      break
    if temp_y in circulation:
      break
    else:
      circulation.add(temp_y)
    cnt += 1

  print(result)