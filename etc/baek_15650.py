# 2022/09/13 Baek 15650

from itertools import combinations

N, M = map(int, input().split())
candidates = sorted(list(combinations(range(1, N + 1), M)))
for candidate in candidates:
  for member in candidate:
    print(member, end = " ")
  print("")