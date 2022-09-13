# 2022/09/13 Baek 15652

from itertools import  combinations_with_replacement

N, M = map(int, input().split())
candidates = sorted(list(combinations_with_replacement(range(1, N + 1), M)))
for candidate in candidates:
  for member in candidate:
    print(member, end = " ")
  print("")