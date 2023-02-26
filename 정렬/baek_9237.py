# 2023/02/24 Baek 9237

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
numbers = [ numbers[i] + i + 1 for i in range(len(numbers))]
print(max(numbers) + 1)