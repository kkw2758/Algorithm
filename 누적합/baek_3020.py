# 2023/03/17 Baek 3020

# N, H = map(int, input().split())

# even = [0] * (H + 1)
# odd = [0] * (H + 1)

# min_count = N  # 파괴해야 하는 장애물의 최소값
# range_count = 0  # 최소값이 나타나는 구간의 수

# for i in range(N):
#     j = int(input())
#     if i % 2 == 0:
#         even[j] += 1
#     else:
#         odd[j] += 1

# for i in range(H - 1, 0, -1):
#     even[i] += even[i + 1]
#     odd[i] += odd[i + 1]

# for i in range(1, H + 1):

#     if min_count > (even[i] + odd[H - i + 1]):
#         min_count = (even[i] + odd[H - i + 1])
#         range_count = 1
#     elif min_count == (even[i] + odd[H - i + 1]):
#         range_count += 1

# print(min_count, range_count)



N, H = map(int, input().split())

odd = [0] * H
even = [0] * H

for i in range(N):
    j = int(input())
    if i % 2 == 0:
        even[j - 1] += 1
    else:
        odd[j - 1] += 1

for i in range(H - 1, 0, -1):
    even[i - 1] += even[i]
    odd[i - 1] += odd[i]

print(even, odd)

result_value = 200001
result_cnt = 0

for i in range(H):
    temp = even[i] + odd[H - 1 - i]
    if temp < result_value:
        result_value = temp
        result_cnt = 0

    if result_value == temp:
        result_cnt += 1

print(result_value, result_cnt)


# import sys
# from bisect import bisect_left

# input = sys.stdin.readline

# N, H = map(int, input().split())
# even = []
# odd = []
# for i in range(N):
#     j = int(input())
#     if i % 2 == 0:
#         even.append(j)
#     else:
#         odd.append(j)

# even.sort()
# odd.sort()

# min_val = int(1e9)
# for i in range(1, H + 1):
#     t, b = bisect_left(even, i), bisect_left(odd, H + 1 - i)
#     temp = N - (t + b)
#     if temp < min_val:
#         min_val = temp
#         cnt = 1
#     elif temp == min_val:
#         cnt += 1
    
# print(min_val, cnt)