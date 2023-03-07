# 2023/03/07 Baek 2559

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    numbers[i] += numbers[i - 1]

result = -int(1e9)
for i in range(K, N + 1):
    result = max(result, numbers[i] - numbers[i - K])

print(result)