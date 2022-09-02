# 2022/09/02 Baek 1620

import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

pocketmons = {}
for idx in range(1, N + 1):
  pocketmons[input().rstrip()] = idx

pocketmons_dict = sorted(list(pocketmons.items()), key=lambda x: x[1])

for _ in range(M):
  query = input().rstrip()
  if query in pocketmons:
    print(pocketmons[query])
  else:
    print(pocketmons_dict[int(query) - 1][0])