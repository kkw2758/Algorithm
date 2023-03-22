# 2023/03/22 Baek 1806

# import sys
# input = sys.stdin.readline

# N, S = map(int, input().split())
# numbers = [0] + list(map(int, input().split()))

# for i in range(1, N + 1):
#     numbers[i] += numbers[i - 1]

# if numbers[-1] < S:
#     print(0)
# else:
#     for interval in range(1, N + 1):
#         for j in range(interval, N + 1):
#             if numbers[j] - numbers[j - interval] >= S:
#                 print(interval)
#                 sys.exit()


import sys
input = sys.stdin.readline

N, S = map(int, input().split())

numbers = list(map(int, input().split()))

left, right = 0, 0
sum = 0
min_length = sys.maxsize

while True:
    if sum >= S:
        min_length = min(min_length, right - left)
        sum -= numbers[left]
        left += 1
    elif right == N:
        break
    else:
        sum += numbers[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)