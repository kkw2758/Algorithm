# 2022/09/13 Baek 15654

from itertools import  permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

candidates = sorted(permutations(numbers, M))
for candidate in candidates:
  for member in candidate:
    print(member, end = " ")
  print("")