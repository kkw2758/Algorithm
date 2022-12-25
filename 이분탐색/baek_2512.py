# 2022/11/24 Baek 2512

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())

start = 0
end = M
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(N):
        if mid <= arr[i]:
            total += mid
        else:
            total += arr[i]

    if total > M:
        end = mid - 1
    else:   # total < M
        result = max(result, mid)
        start = mid + 1

max_value = max(arr)

if max_value > result:
    print(result)
else:   # max_value <= result
    print(max_value)