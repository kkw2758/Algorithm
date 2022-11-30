# 2022/11/28 Baek 11501
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input())
  numbers = list(map(int, input().split()))
  result = 0

  max_value = numbers[N -1]
  for i in range(N - 2, -1, -1):
    if max_value > numbers[i]:
      result += max_value - numbers[i]
    elif max_value < numbers[i]:
      max_value = numbers[i]

  print(result)