# 2022/09/25 Baek 2294

# k의 범위 1 <= k <= 10000
# 2차원 배열 생성시 1억개의 공간만들어져서 메모리초과 발생
# 3중 for문 이용시 시간초과 발생

# INF = int(1e9)
# n, k = map(int, input().split())
# ary = []

# dp = [0] * (k + 1)

# for _ in range(n):
#   coin_value = int(input())
#   if coin_value < k + 1:
#     dp[coin_value] = 1
#     ary.append(coin_value)

# def solve():
#   global dp
#   for i in range(2, k + 1): # i개 가지고 만들경우
#     temp = [0] * (k + 1)
#     for j in ary:
#       for m in range(1, k + 1 - j):
#         if dp[m] != 0:
#           if m + j <= k:
#             temp[m + j] += 1
#             if m + j == k:
#               return i
#     dp = temp
#   return -1

# print(solve())

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

li =[]

for i in range(n):
   li.append(int(input().rstrip()))

dp = [10001] * (k+1)
dp[0] = 0

for num in li:
   for i in range(num, k+1):
       dp[i] = min(dp[i], dp[i-num]+1)

if dp[k] == 10001:
   print(-1)
else:
   print(dp[k])