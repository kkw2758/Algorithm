# 2023/04/03 Baek 3273

# n 개의 서로 다른 "양의 정수"
# 모든 경우를 다 고려하면 시간초과 남

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
numbers.sort()

left = 0
right = n - 1
result = 0

while left < right:
    if numbers[left] + numbers[right] > x:
        right -= 1
    elif numbers[left] + numbers[right] == x:
        result += 1
        left += 1
    else:
        left += 1
print(result)
    