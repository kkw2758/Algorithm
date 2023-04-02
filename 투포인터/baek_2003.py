# 2023/04/01 Baek 2003

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

start = 0
end = 0

total = numbers[0]
result = 0
while True:
    if total == M:
        result += 1
        total -= numbers[start]
        start += 1
    elif total > M:
        total -= numbers[start]
        start += 1
    else:
        end += 1
        if end >= N:
            break
        total += numbers[end]
        

print(result)