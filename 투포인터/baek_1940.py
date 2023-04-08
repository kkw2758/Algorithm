# 2023/04/04 Baek 1940

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

left = 0
right = N - 1

result = 0
while left < right:
    if numbers[left] + numbers[right] == M:
        result += 1
        left += 1
        right -= 1
    elif numbers[left] + numbers[right] > M:
        right -= 1
    elif numbers[left] + numbers[right] < M:
        left += 1


print(result)