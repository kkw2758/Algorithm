# 2023/02/17 Baek 11931

import sys
input = sys.stdin.readline

N = int(input())
numbers = []
numbers.
for _ in range(N):
  numbers.append(int(input()))

numbers.sort(reverse=True)

for number in numbers:
  print(number)