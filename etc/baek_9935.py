# # 2023/04/28 Baek 9935
# # 시간 제한 2초

# # 문자열의 길이는 1보다 크거나 같고, 1000000보다 작거나 같다.
# # 문자열은 알파벳 소문자와 대문자, 숫자 0 ~ 9 로만 이루어져있다.
# # 폭발 문자열의 길이는 1보다 크거나 같고, 36보다 작거나 같다.

# import sys
# input = sys.stdin.readline

# string = input().strip()
# bomb_string = input().strip()

# # 순차탐색하면서 폭발 문자열을 제거

# # 아디이어
# # 이분탐색의 lower_bound를 이용한다 -> 문자열이 정렬되어 있지 않으므로 안됨
# # 검사 시작점을 start라고 놓고 탐색
# # 폭발 문자열을 만나면 제거하고 다시 탐색을 진행해야하는데
# # 이과정에서 start 인덱스르 다시 뒤로 조정해야하는 과정이 생겨서 시간초과가 남

# # 시간초과.
# start = 0
# bomb_len = len(bomb_string)
# while start < len(string):
#     if string[start] == bomb_string[0]:
#         # 만약 폭발 문자열을 찾으면
#         if string[start: start + bomb_len] == bomb_string:
#             string = string[:start] + string[start + bomb_len:]

#             start -= (bomb_len - 1)
#             if start < 0:
#                 start = 0
#         else:
#             start += 1
#     else:
#         start += 1
        
# if string:
#     print(string)
# else:
#     print("FRULA")
    

# # 풀이참고
# # https://velog.io/@heejun32/%EB%B0%B1%EC%A4%80-9935%EB%B2%88-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8F%AD%EB%B0%9C-Python
import sys
input = sys.stdin.readline

S = input().rstrip()
explosion_string = input().rstrip()

# stack으로 문자열 폭발 구현
stack = []
ex_len = len(explosion_string)

for i in range(len(S)):
    print(i)
    stack.append(S[i])
    if ''.join(stack[-ex_len:]) == explosion_string:
        for _ in range(ex_len):
            stack.pop()
            
if stack:
    print("".join(stack))
else:
    print("FRULA")
    
# 풀이를 보고 내생각
import sys
input = sys.stdin.readline

string = input().rstrip()
bomb_string = input().rstrip()


bomb_len = len(bomb_string)
start = 0
cnt = 0
while start < len(string) - 1:
    print(cnt)
    cnt += 1
    start += 1
    # 만약 폭발 문자열을 찾으면
    # print(string[start - bomb_len + 1 : start + 1])
    if string[start] == bomb_string[-1]:
        if string[start - bomb_len + 1 : start + 1] == bomb_string:
            string = string[:start - bomb_len + 1] + string[start + 1:]
            start -= bomb_len
if string:
    print(string)
else:
    print("FRULA")