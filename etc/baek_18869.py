# # 2022/11/19 Baek 18869

# import sys

# N, M = map(int, input().split())
# planets = [[] for _ in range(N)]
# for i in range(N):
#   temp = []
#   planet_weights = list(map(int, input().split()))
#   for idx, weight in enumerate(planet_weights):
#     temp.append((weight, idx))
#   temp.sort()
#   for j in range(M):
#     planets[i].append(temp[j][1])

# cnt = 0
# for i in range(N):
#   for j in range(i + 1, N):
#     if planets[i] == planets[j]:
#       cnt += 1

# print(cnt)

import sys
input = sys.stdin.readline
from collections import defaultdict

m, n = map(int, input().split())
universe = defaultdict(int)
for _ in range(m):
    planets = list(map(int, input().split()))
    keys = sorted(list(set(planets)))
    ranks = {keys[i]: i for i in range(len(keys))}
    add = tuple([ranks[x] for x in planets])
    universe[add] += 1
ans = 0
for cnt in universe.values():
    ans += cnt * (cnt - 1) // 2
print(ans)