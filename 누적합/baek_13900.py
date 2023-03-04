# 2023/03/04 Baek 13900

import sys
input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().split()))

result = 0

for i in range(1, N + 1):
    numbers[i] += numbers[i - 1]

for i in range(1, N):
    result += (numbers[i] - numbers[i - 1]) * (numbers[N] - numbers[i])

print(result)