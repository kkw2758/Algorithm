# 2023/02/13 Baek 10867

N = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(list(set(numbers)))
for number in numbers:
  print(number, end = " ")