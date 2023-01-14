# N = int(input())
# numbers = list(map(int, input().split()))

# number_group = []

# temp = []
# for i in range(N):
#   if not temp:
#     temp.append(numbers[i])
#     continue
  
#   if numbers[i] - temp[-1] == 1:
#     temp.append(numbers[i])
#   else:
#     number_group.append(temp)
#     temp = [numbers[i]]

# number_group.append(temp)

# result = 0
# for group in number_group:
#   result += group[0]

# print(result)



# 딸기, 바나나, 라임, 자두
# import sys
# input = sys.stdin.readline

# N = int(input())
# fruit_dict = {"STRAWBERRY" : 0, "BANANA" : 1, "LIME" : 2, "PLUM" : 3}
# fruit_cnt = [0, 0, 0, 0]

# for i in range(N):
#   fruit, cnt = input().strip().split()
#   cnt = int(cnt)
#   fruit_cnt[fruit_dict[fruit]] += cnt

# flag = False
# for i in range(4):
#   if fruit_cnt[i] == 5:
#     flag = True
#     break

# if flag:
#   print("YES")
# else:
#   print("NO")

# import sys
# input = sys.stdin.readline

# N = int(input())

# reverse = False
# time = 0

# for i in range(N):
#   type, number = input().strip().split()
#   number = int(number)
#   if reverse:
#     time = (time - 1) % 12
#   else:
#     time = (time + 1) % 12

#   if time == 0:
#     time = 12

#   if type == "HOURGLASS":
#     if reverse:
#       if time == number:
#         print(time, "NO")
#         continue
#       else:
#         print(time, "NO")
#     else:
#       if time == number:
#         print(time, "NO")
#         continue
#       else:
#         print(time, "NO")
#     reverse = not(reverse)
#   else:
#     if reverse:
#       if time == number:
#         print(time, "YES")
#       else:
#         print(time, "NO")
#     else:
#       if time == number:
#         print(time, "YES")
#       else:
#         print(time, "NO")


# from itertools import combinations_with_replacement

# flag = input()
# fixed_numbers = list(map(int, input().split()))

# def one_to_six(fixed_number, number):
#   result = 0
#   for i in fixed_number:
#     if i == number:
#       result += number
#   return result

# def Four_of_a_Kind(fixed_number):
#   numbers_cnt = [0] * 7
#   for i in fixed_number:
#     numbers_cnt[i] += 1

#   for i in range(1, 7):
#     if numbers_cnt[i] >= 4:
#       return i * 4
  
#   return 0

# def Full_house(fixed_number):
#   numbers_cnt = [0] * 7
#   for i in fixed_number:
#     numbers_cnt[i] += 1

#   flag = False
#   one_flag = False
#   for i in range(1, 7):
#     if numbers_cnt[i] == 2:
#       one_flag = True
#     if numbers_cnt[i] == 3:
#       flag = True

#   if flag and one_flag:
#     return sum(fixed_number)
#   else:
#     return 0


# def Little_Straight(fixed_number):
#   numbers_cnt = [0] * 7
#   for i in fixed_number:
#     numbers_cnt[i] += 1

#   for i in range(1, 6):
#     if numbers_cnt[i] != 1:
#       return 0
  
#   return 30

# def Big_Straight(fixed_number):
#   numbers_cnt = [0] * 7
#   for i in fixed_number:
#     numbers_cnt[i] += 1

#   for i in range(2, 7):
#     if numbers_cnt[i] != 1:
#       return 0
  
#   return 30

# def Yacht(fixed_number):
#   numbers_cnt = [0] * 7
#   for i in fixed_number:
#     numbers_cnt[i] += 1

#   for i in range(1, 7):
#     if numbers_cnt[i] == 5:
#       return 50
  
#   return 0

# def Choice(fixed_number):
#   result = 0
#   for i in fixed_number:
#     result += i
  
#   return result


# candidates = list(combinations_with_replacement(list(range(1, 7)), 2))

# result = 0
# for candidate in candidates:
#   candidate = fixed_numbers + list(candidate)
#   # print(candidate)
#   for i in range(12):
#     if flag[i] == "Y":
#       if 0 <= i < 6:
#         result = max(result, one_to_six(candidate, i + 1))
#         # print(i, result)
#         continue
#       if i == 6:
#         result = max(result, Four_of_a_Kind(candidate))
#         # print(i, result)
#         continue
#       if i == 7:
#         result = max(result, Full_house(candidate))
#         # print(i, result)
#         continue
#       if i == 8:
#         result = max(result, Little_Straight(candidate))
#         # print(i, result)
#         continue
#       if i == 9:
#         result = max(result, Big_Straight(candidate))
#         # print(i, result)
#         continue
#       if i == 10:
#         result = max(result, Yacht(candidate))
#         # print(i, result)
#         continue
#       if i == 11:
#         result = max(result, Choice(candidate))
#         # print(i, result)
#         continue
    
# print(result)


# import sys
# input = sys.stdin.readline

# N = int(input())
# numbers = list(map(int, input().strip().split()))
# # 인덱스 매칭 dict
# dict = {}
# result = [0] * N

# for i in range(len(numbers)):
#   dict[numbers[i]] = i

# for i in numbers:
#   cnt = 2
#   while i * cnt <= 1000000:
#     if i * cnt in dict:
#       result[dict[i]] += 1
#       result[dict[i * cnt]] -= 1
#     cnt += 1

# for i in result:
#   print(i, end = " ")


# N = int(input())
# horse_cnt = list(map(int, input().split()))
# x = int(input())

# def solve():
#   one_index = []
#   for i in range(N + 1):
#     if len(one_index) > 2:
#       print("NO")
#       return
#     if horse_cnt[i] == 1:
#       one_index.append(i)

#   # 1자리가 두개
#   if len(one_index) == 2:
#     if abs(one_index[0] - one_index[1]) == x:
#       print("YES")
#       print(one_index[0], one_index[1])
#       return
#     else:
#       print("NO")
#       return

#   # 불안전한 자리 한개
#   if len(one_index) == 1:
#     if one_index[0] - x >= 0:
#       if horse_cnt[one_index[0] - x] > 2:
#         print("YES")
#         print(one_index[0] - x, one_index[0])
#         return
#     if one_index[0] + x <= N:
#       if horse_cnt[one_index[0] + x] != 0:
#         print("YES")
#         print(one_index[0], one_index[0] + x)
#         return
#     print("NO")
#     return

#   # 1 자리 0개
#   for i in range(N - x + 1):
#     if horse_cnt[i] > 2 and horse_cnt[i + x] >= 1:
#       print("YES")
#       print(i, i + x)
#       return

#   print("NO")

# solve()

from collections import deque
import sys
input = sys.stdin.readline

N, A, L = map(int, input().strip().split())
attack = []
for i in range(N):
  x, y = map(int, input().split())
  attack.append((x, y))

q = deque()
q.append((A, L, ""))

is_end = False

while q:
  x, y, flag = q.popleft()
  # print("x, y, flag",x, y, flag)
  if len(flag) == N:
    is_end = True
    print("YES")
    print(flag)
    break
  ax, ay = attack[len(flag)]
  # print("ax, ay",ax, ay)
  if ax >= 0 and ay >= 0:
    if x < ax:
      # 라이프 0
      if x < ax:
        if y - ay > 0:
          q.append((x, y - ay, flag + "L"))
    else:
      if y - ay > 0:
        q.append((x, y - ay, flag + "L"))

      q.append((x - ax, y, flag + "A"))
    
  if ay == -1:
    q.append((max(x - ax, 0), y, flag + "A"))
  

  if ax == -1:
    if x - ax > 0:
      q.append((x - ax, y, flag + "L"))

if not(is_end):
  print("NO")