# 2023/02/02 Baek 11651

import sys
input = sys.stdin.readline

N = int(input())

indexes = []
for _ in range(N):
    indexes.append((list(map(int, input().split()))))

indexes.sort(key = lambda x: (x[1], x[0]))
for x, y in indexes:
    print(x, y)