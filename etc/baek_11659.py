# 2022/09/03 Baek 11659

import sys

inpurt = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]

for i in range(1, len(numbers)):
  numbers[i] = numbers[i] + numbers[i - 1]

numbers = [0] + numbers
for _ in range(M):
  i, j = map(int, input().split())
  print(prefix_sum[j] - prefix_sum[i - 1])