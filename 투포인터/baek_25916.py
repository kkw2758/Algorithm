# 2023/02/10 Baek 25916

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

result = 0
start = 0
end = 0
interval_sum = 0

# 투 포인터
for start in range(N):
    while interval_sum < M and end < N:
        
        interval_sum += A[end]
        end += 1

    if interval_sum <= M:
        result = max(result, interval_sum)
    else:
        result = max(result, interval_sum - A[end - 1])
    interval_sum -= A[start]

print(result)

# 투포인터 연습

# n = 5
# m = 5
# data = [1,2,3,2,5]

# count = 0
# interval_sum = 0
# end = 0
# for start in range(n):
#     while interval_sum < m and end < n:
#         interval_sum += data[end]
#         end += 1

#     if interval_sum == m:
#         print(start, end)
#         count += 1
#     interval_sum -= data[start]

# print(count)