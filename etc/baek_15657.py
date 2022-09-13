# 2022/09/13 Baek 15657

from itertools import  combinations_with_replacement

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

candidates = combinations_with_replacement(numbers, M)
for candidate in candidates:
  for member in candidate:
    print(member, end = " ")
  print("")