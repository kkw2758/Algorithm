# 2023/01/31 Baek 11650

import sys
input = sys.stdin.readline

N = int(input())
indexes = []
for _ in range(N):
    indexes.append(list(map(int, input().split())))


indexes.sort(key = lambda x : (x[0], x[1]))

for x, y in indexes:
    print(x, y)