# 2023/03/28 Baek 19951

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))

temp = [0] * (N + 1)

for _ in range(M):
    a, b, k = map(int, input().split())
    temp[a - 1] += k
    temp[b] -= k
tmp = 0
for i in range(N):
    tmp += temp[i]
    heights[i] += tmp

for height in heights:
    print(height, end = " ")
