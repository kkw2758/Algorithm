# 2023/04/13 Baek 17609

# 나의 1차 풀이
# 반례존재 aapqbcbqpqaa > 2
# T = int(input())
# for _ in range(T):
#   target = input()
#   start = 0
#   end = len(target) - 1

#   remove_flag = False
#   etc_flag = False
#   while start < end:
#     if target[start] == target[end]:
#       start += 1
#       end -= 1
#     else: # 두개가 다를때
#       if remove_flag == True: # 이미 하나 제거했으니까
#         etc_flag = True
#         break
#       else:
#         if target[start + 1] == target[end] or target[start] == target[end - 1]:
#           print("A")
#           if target[start + 1] == target[end]:
#             print("left")
#             start += 2
#             end -= 1
#             remove_flag = True
#           else:
#             print("right")
#             start += 1
#             end -= 2
#             remove_flag = True
#         else:
#           remove_flag = True
#           etc_flag = True
#           break

#   if remove_flag == False:
#     print(0)
#   elif etc_flag == False:
#     print(1)
#   else:
#     print(2)

def finalCheck(str, left, right):
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def checkIsSame(str, left, right):
    if str == str[::-1]: # 바로 화문인 경우
        return 0
    while left < right: # 1 or 2
        if str[left] == str[right]: # 같으면 한칸씩 이동
            left += 1
            right -= 1
        else:
            leftCheck = finalCheck(str, left + 1, right) # 왼쪽 한칸 건너뜀
            rightCheck = finalCheck(str, left, right-1) # 오른쪽 한칸 건너뜀
            if leftCheck or rightCheck: # 다른 문자 안나왔으면 회문임
                return 1
            else: # 다른 문자 나온 경우
                return 2
    return 1
    
t = int(input())

for i in range(t):
    str = input()
    print(checkIsSame(str, 0, len(str)-1))



import sys

def is_palindrome(str_):
    left = 0
    right = len(str_) - 1
    while left < right:
        # 1. left right 문자가 동일한 경우:  left + 1, right + 1
        if str_[left] == str_[right]:
            left += 1
            right -= 1
        else:
            # 2. left right 다른 경우: 한 문자열 제거 후 회문 확인
            # 2-1. 오른쪽 문자열 제거한 경우 제거 후 회문이되는지 확인 

            temp = str_[:right] + str_[right + 1:]
            if temp[:] == temp[::-1]:
                return 1
            # 2-2. 왼쪽 문자열 제거한 경우 제거 후 회문이되는지 확인 

            temp = str_[:left] + str_[left + 1:]
            if temp[:] == temp[::-1]:
                return 1
            # # 2-3. 회문이 안된 경우, 2리턴  
            return 2
        
    return 0

for _ in range(int(sys.stdin.readline())):
    print(is_palindrome(sys.stdin.readline().strip()))