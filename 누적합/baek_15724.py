# 2023/03/22 Baek 15724

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ary = [[0] * (M + 1)]
for _ in range(N):
    ary.append([0] + list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, M + 1):
        ary[i][j] += ary[i - 1][j] + ary[i][j - 1] - ary[i - 1][j - 1]

K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = list(map(int, input().split()))
    print(ary[x2][y2] - ary[x2][y1 - 1] - ary[x1 - 1][y2] + ary[x1 - 1][y1 - 1])
